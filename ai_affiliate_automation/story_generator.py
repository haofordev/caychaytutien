import os
import sys
import json
from pathlib import Path
import openai
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Load environment variables for API keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not OPENAI_API_KEY and not GEMINI_API_KEY:
    raise RuntimeError("Please set either OPENAI_API_KEY or GEMINI_API_KEY environment variable")

def generate_story(prompt: str) -> dict:
    """Generate a Vietnamese story using the selected LLM.
    Returns a dict matching the existing Story Bible schema plus a simple list of scenes.
    """
    # Use OpenAI if available, otherwise Gemini via placeholder
    if OPENAI_API_KEY:
        client = openai.OpenAI(api_key=OPENAI_API_KEY)
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "system", "content": "Bạn là một tác giả viết truyện xianxia ngắn gọn, tạo story bible JSON cho một video 60 giây."},
                      {"role": "user", "content": f"{prompt}"}],
            max_tokens=1500,
            temperature=0.8,
        )
        content = response.choices[0].message.content
    else:
        # Placeholder for Gemini – you would replace this with the actual call
        raise NotImplementedError("Gemini call not implemented in this example")
    # Expect the model to return a JSON block
    try:
        story = json.loads(content)
    except json.JSONDecodeError:
        # Fallback: wrap raw text in a simple schema
        story = {
            "title": prompt,
            "logline": "",
            "genre_tags": [],
            "world": {},
            "main_character": {},
            "factions": [],
            "villain_arcs": [],
            "artifacts_and_skills": [],
            "central_mystery": "",
            "first_three_chapters_hook": [],
            "scenes": [
                {"description": "Intro scene", "duration": 5},
                {"description": "Middle conflict", "duration": 45},
                {"description": "Cliffhanger CTA", "duration": 10}
            ]
        }
    return story

def main():
    if len(sys.argv) < 2:
        print("Usage: python story_generator.py \"<idea>\"")
        sys.exit(1)
    prompt = sys.argv[1]
    story = generate_story(prompt)
    output_dir = Path(__file__).parent / "output"
    output_dir.mkdir(parents=True, exist_ok=True)
    story_path = output_dir / "story.json"
    story_path.write_text(json.dumps(story, ensure_ascii=False, indent=2))
    print(f"Story generated and saved to {story_path}")

if __name__ == "__main__":
    main()
