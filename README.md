# Conspiracy Theory Generator

A CLI tool that takes any everyday object and generates an elaborate, deadpan-serious conspiracy theory about it using the Claude API. Funny, not mean — no real people, companies, or groups.

## Setup

1. Clone the repo and install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Create a `.env` file with your Anthropic API key:
   ```
   ANTHROPIC_API_KEY=your_key_here
   ```

## Usage

```bash
# Basic usage
python conspiracy.py "stapler"

# Interactive mode (no argument — will prompt you)
python conspiracy.py

# Pick a random object
python conspiracy.py --random

# Change paranoia level: mild / standard (default) / unhinged
python conspiracy.py "traffic cone" --paranoia unhinged

# Save the theory to theories.txt
python conspiracy.py "microwave" --save

# Combine flags
python conspiracy.py --random --paranoia mild --save
```

## Sample Output

```
============================================================
  CLASSIFIED: THE TRUTH ABOUT STAPLER
============================================================

In 1987, the Bureau of Organizational Compliance quietly commissioned
Project BIND — a decade-long initiative to embed passive behavioral
conditioning into standard office equipment. The stapler was chosen
for its ubiquity and its underestimated grip on the human psyche.

Declassified memos from the Morrow Institute (obtained through a
whistleblower in 2019) reveal that the rhythmic click of the stapler
activates a micro-compliance response in the prefrontal cortex. Each
press reinforces docility. Each jam — carefully engineered — triggers
controlled frustration, priming workers to accept authoritarian
correction.

Connect the dots: why does every open-plan office have seventeen
staplers but only one person who knows where they are? Follow the
supply chain. Follow the chrome. The paper isn't the only thing
being bound.

They gave you the stapler. They kept the key.

Wake up.

============================================================
```

## Paranoia Levels

| Level | Description |
|-------|-------------|
| `mild` | Measured, analytical, quietly suspicious |
| `standard` | Classic conspiracy tone — escalating evidence, ominous ending |
| `unhinged` | Maximum urgency, interlocking networks, civilization-level stakes |

## Files

- `conspiracy.py` — main CLI entry point
- `requirements.txt` — Python dependencies
- `.env` — your API key (not committed)
- `theories.txt` — your saved case file (created by `--save`, not committed)
