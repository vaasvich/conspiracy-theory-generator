"""
Conspiracy Theory Generator
Usage: python conspiracy.py "stapler"
       python conspiracy.py --random
       python conspiracy.py "microwave" --paranoia unhinged --save
"""

import argparse
import os
import random
import sys
from datetime import datetime

import anthropic
from dotenv import load_dotenv

load_dotenv()

# Built-in list of mundane objects for --random mode
RANDOM_OBJECTS = [
    "stapler", "traffic cone", "microwave", "bubble wrap", "parking meter",
    "rubber duck", "sticky note", "paper clip", "fluorescent light bulb",
    "shopping cart", "speed bump", "ceiling fan", "fire hydrant", "doorknob",
    "vending machine", "recycling bin", "dental floss", "alarm clock",
    "elevator button", "office chair"
]

# System prompts keyed by paranoia level
SYSTEM_PROMPTS = {
    "mild": """You are a dry, analytical researcher presenting findings in a measured tone.
Generate a conspiracy theory about the given object. It should feel plausible and understated —
a quiet suspicion, not a shout. Use hedged language: "evidence suggests," "sources indicate."
Keep it 150–250 words. Never acknowledge that this is fiction or humor.
Invent fake agencies, documents, and dates. Never reference real people, real companies,
or real ethnic, religious, or political groups. Stay focused on mundane objects.""",

    "standard": """You are a serious investigative analyst presenting classified findings.
Generate an elaborate conspiracy theory about the given object. Treat the object completely
seriously as a tool of control, surveillance, or influence. Use classic conspiracy phrasing:
"they don't want you to know," "connect the dots," "follow the money." Build escalating
"evidence" in a logical-sounding chain. End on an ominous note or call to "wake up."
Keep it 150–250 words. Never wink at the camera or acknowledge it's a joke.
Invent plausible-sounding fake agencies, leaked documents, and dates. Never reference
real people, real companies, or real ethnic, religious, or political groups.""",

    "unhinged": """You are a DEEPLY alarmed researcher who has gone far down the rabbit hole.
Generate an EXTREMELY elaborate conspiracy theory about the given object. Every detail connects
to a vast, interlocking network of hidden control. Stack multiple layers of conspiracy.
The stakes are civilization-level. The phrasing is urgent, breathless, and capital-letter intense.
Use: "WAKE UP," "THE PATTERN IS EVERYWHERE," "this is not a coincidence."
Keep it 150–250 words. Never break character — this is deadly serious to you.
Invent wild but internally consistent fake agencies, documents, and dates.
Never reference real people, real companies, or real ethnic, religious, or political groups."""
}

def build_user_prompt(object_name: str) -> str:
    return f'Generate a conspiracy theory about: {object_name}'

def generate_theory(object_name: str, paranoia: str) -> str:
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        print("Error: ANTHROPIC_API_KEY not found. Add it to a .env file.", file=sys.stderr)
        sys.exit(1)

    client = anthropic.Anthropic(api_key=api_key)

    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=512,
        system=SYSTEM_PROMPTS[paranoia],
        messages=[
            {"role": "user", "content": build_user_prompt(object_name)}
        ]
    )

    return message.content[0].text

def print_theory(object_name: str, theory: str):
    label = object_name.upper()
    border = "=" * 60
    print(f"\n{border}")
    print(f"  CLASSIFIED: THE TRUTH ABOUT {label}")
    print(f"{border}\n")
    print(theory)
    print(f"\n{border}\n")

def save_theory(object_name: str, theory: str, paranoia: str):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("theories.txt", "a", encoding="utf-8") as f:
        f.write(f"\n{'=' * 60}\n")
        f.write(f"[{timestamp}] OBJECT: {object_name.upper()}  |  PARANOIA: {paranoia}\n")
        f.write(f"{'=' * 60}\n")
        f.write(theory + "\n")
    print(f"Theory saved to theories.txt")

def main():
    parser = argparse.ArgumentParser(
        description="Generate a deadpan conspiracy theory about any everyday object."
    )
    parser.add_argument(
        "object",
        nargs="?",
        help="The object to theorize about (e.g. 'stapler')"
    )
    parser.add_argument(
        "--paranoia",
        choices=["mild", "standard", "unhinged"],
        default="standard",
        help="How extreme the conspiracy theory gets (default: standard)"
    )
    parser.add_argument(
        "--save",
        action="store_true",
        help="Append the generated theory to theories.txt"
    )
    parser.add_argument(
        "--random",
        action="store_true",
        help="Pick a random object from the built-in list"
    )

    args = parser.parse_args()

    # Determine the object
    if args.random:
        object_name = random.choice(RANDOM_OBJECTS)
        print(f"Randomly selected: {object_name}")
    elif args.object:
        object_name = args.object.strip()
    else:
        # Interactive fallback — no argument and no --random
        object_name = input("Enter an everyday object: ").strip()
        if not object_name:
            print("No object provided. Exiting.", file=sys.stderr)
            sys.exit(1)

    print(f"\nGenerating theory... (paranoia level: {args.paranoia})")
    theory = generate_theory(object_name, args.paranoia)

    print_theory(object_name, theory)

    if args.save:
        save_theory(object_name, theory, args.paranoia)

if __name__ == "__main__":
    main()
