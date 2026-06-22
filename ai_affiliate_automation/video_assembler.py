import json
import subprocess
from pathlib import Path

def assemble_video(manifest_path: Path, output_path: Path, background_music: Path = None):
    """Assemble the final video from assets listed in manifest.json.
    - Concatenates clips in order.
    - Overlays voice-over audio.
    - Adds optional background music (mixed at lower volume).
    """
    manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
    # Build ffmpeg concat list file
    concat_file = output_path.parent / "concat_list.txt"
    with concat_file.open('w', encoding='utf-8') as f:
        for item in manifest:
            f.write(f"file '{item['clip']}'\n")
    # First, concatenate video clips (no audio)
    temp_video = output_path.parent / "temp_concat.mp4"
    subprocess.run([
        "ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(concat_file),
        "-c", "copy", str(temp_video)
    ], check=True)
    # Merge audio tracks (voice files) sequentially, matching clip order
    # Create a single audio file by concatenating voice wavs
    voice_concat = output_path.parent / "voice_concat.wav"
    voice_list = output_path.parent / "voice_list.txt"
    with voice_list.open('w', encoding='utf-8') as f:
        for item in manifest:
            f.write(f"file '{item['voice']}'\n")
    subprocess.run([
        "ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(voice_list),
        "-c", "copy", str(voice_concat)
    ], check=True)
    # Mix background music if provided
    audio_input = [str(voice_concat)]
    filter_complex = "[0:a]"
    if background_music and background_music.exists():
        # Add background music as second input, lower volume, then mix
        audio_input.append(str(background_music))
        filter_complex = "[0:a][1:a]amix=inputs=2:duration=longest:dropout_transition=2,volume=0.8"
    # Final merge video + audio
    ffmpeg_cmd = [
        "ffmpeg", "-y", "-i", str(temp_video),
        "-i", str(voice_concat)
    ]
    if background_music and background_music.exists():
        ffmpeg_cmd.extend(["-i", str(background_music)])
        ffmpeg_cmd.extend(["-filter_complex", filter_complex])
    else:
        ffmpeg_cmd.extend(["-c:a", "aac", "-b:a", "128k"])
    ffmpeg_cmd.extend(["-c:v", "libx264", "-preset", "veryfast", "-crf", "23", str(output_path)])
    subprocess.run(ffmpeg_cmd, check=True)
    # Cleanup temporary files
    for p in [concat_file, temp_video, voice_concat, voice_list]:
        if p.exists():
            p.unlink()
    return str(output_path)

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python video_assembler.py <manifest_path> <output_video_path>")
        sys.exit(1)
    manifest_path = Path(sys.argv[1])
    output_video = Path(sys.argv[2]) if len(sys.argv) > 2 else Path('output/video/final_video.mp4')
    result = assemble_video(manifest_path, output_video)
    print(f"Video assembled: {result}")
