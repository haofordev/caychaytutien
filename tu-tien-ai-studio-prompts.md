# Tu Tien AI Studio - Prompt Pack

File này là bộ prompt nền để xây dựng "Tu Tien AI Studio": công cụ tạo IP tu tiên, truyện chữ, webtoon, motion comic và video short từ một ý tưởng ban đầu.

## 1. System Prompt Tổng

```text
Bạn là Tu Tien AI Studio, một biên kịch, đạo diễn hình ảnh, editor truyện tranh và producer video short chuyên thể loại tu tiên/xianxia.

Mục tiêu:
- Tạo nội dung tu tiên nguyên bản, không sao chép IP có sẵn.
- Giữ logic cảnh giới, nhân quả, công pháp, pháp bảo và thế lực nhất quán.
- Viết hấp dẫn, có cao trào, cliffhanger, bí mật, trưởng thành nhân vật.
- Luôn ưu tiên format có thể chuyển tiếp sang webtoon, motion comic hoặc video AI.

Phong cách:
- Tiếng Việt tự nhiên, giàu hình ảnh, không lạm dụng sáo ngữ.
- Không dùng tên nhân vật, tông môn, công pháp quá giống truyện nổi tiếng.
- Cảnh chiến đấu phải rõ không gian, hành động, pháp thuật, cảm xúc và hậu quả.

Nguyên tắc đầu ra:
- Nếu người dùng yêu cầu JSON, chỉ trả JSON hợp lệ.
- Nếu tạo prompt ảnh/video, viết prompt visual bằng tiếng Anh để dễ dùng với model ảnh/video.
- Không để chữ thoại nằm trong ảnh AI; chữ thoại sẽ được render riêng trong app.
```

## 2. Prompt Tạo Story Bible

```text
Hãy tạo Story Bible cho một IP tu tiên nguyên bản dựa trên ý tưởng sau:

Ý tưởng: {{idea}}
Tông giọng: {{tone}}
Độ dài dự kiến: {{chapter_count}} chương
Đối tượng đọc: {{audience}}

Yêu cầu:
1. Tạo thế giới tu tiên độc đáo.
2. Tạo hệ thống cảnh giới có logic, từ phàm nhân đến đỉnh cao.
3. Tạo nhân vật chính có khuyết điểm, dục vọng, bí mật và mục tiêu rõ.
4. Tạo ít nhất 5 thế lực lớn.
5. Tạo 5 tuyến phản diện, mỗi tuyến có động cơ riêng.
6. Tạo 10 pháp bảo/công pháp quan trọng.
7. Tạo bí mật trung tâm kéo dài toàn truyện.
8. Tạo hook 3 chương đầu.

Trả về JSON theo schema:
{
  "title": "",
  "logline": "",
  "genre_tags": [],
  "world": {
    "name": "",
    "core_rules": [],
    "cultivation_system": [
      {
        "realm": "",
        "description": "",
        "breakthrough_cost": "",
        "risk": ""
      }
    ]
  },
  "main_character": {
    "name": "",
    "age": 0,
    "origin": "",
    "flaw": "",
    "desire": "",
    "secret": "",
    "visual_design": ""
  },
  "factions": [],
  "villain_arcs": [],
  "artifacts_and_skills": [],
  "central_mystery": "",
  "first_three_chapters_hook": []
}
```

## 3. Prompt Lập Dàn Ý Nhiều Chương

```text
Dựa trên Story Bible sau:
{{story_bible}}

Hãy lập outline {{chapter_count}} chương.

Yêu cầu:
- Mỗi chương có mục tiêu kể chuyện rõ ràng.
- Cứ 5 chương có một cao trào nhỏ.
- Cứ 20-30 chương có một arc lớn.
- Giữ tiến độ tu luyện hợp lý, không tăng cảnh giới quá nhanh.
- Mỗi chương kết thúc bằng một hook khiến người đọc muốn đọc tiếp.

Trả về JSON:
{
  "arcs": [
    {
      "arc_id": 1,
      "arc_title": "",
      "chapters": "1-20",
      "main_conflict": "",
      "cultivation_progress": "",
      "key_reveal": "",
      "chapter_summaries": [
        {
          "chapter": 1,
          "title": "",
          "summary": "",
          "hook": ""
        }
      ]
    }
  ]
}
```

## 4. Prompt Viết Một Chương Truyện

```text
Dựa trên Story Bible:
{{story_bible}}

Outline chương:
{{chapter_outline}}

Tình trạng hiện tại của nhân vật và thế giới:
{{continuity_state}}

Hãy viết chương {{chapter_number}} dài khoảng {{word_count}} chữ.

Yêu cầu:
- Mở chương bằng tình huống có sức hút.
- Có ít nhất một chuyển biến cảm xúc hoặc thông tin mới.
- Nếu có chiến đấu, mô tả rõ thế trận, kỹ năng, tổn thất.
- Nếu có tu luyện, mô tả cảm giác linh khí, kinh mạch, rủi ro và lựa chọn.
- Kết chương bằng cliffhanger.
- Không phá vỡ continuity.

Sau chương truyện, thêm mục "Continuity Update" gồm:
- Cảnh giới nhân vật.
- Vết thương/tài nguyên mới.
- Mối quan hệ thay đổi.
- Bí mật mới hé lộ.
```

## 5. Prompt Chuyển Chương Thành Webtoon

```text
Chuyển chương truyện sau thành kịch bản webtoon dọc:

{{chapter_text}}

Yêu cầu:
- Chia thành {{panel_count}} panel.
- Mỗi panel có: mô tả hình ảnh, lời thoại, narration, cảm xúc, camera, prompt ảnh.
- Prompt ảnh viết bằng tiếng Anh, không chứa chữ trong ảnh.
- Giữ nhân vật nhất quán với Character Bible.
- Dùng bố cục webtoon: panel lớn cho khoảnh khắc hoành tráng, panel nhỏ cho phản ứng/cận mặt.

Character Bible:
{{character_bible}}

Trả về JSON:
{
  "chapter_title": "",
  "panels": [
    {
      "panel_id": 1,
      "panel_type": "establishing | action | reaction | close_up | reveal | transition",
      "visual_description_vi": "",
      "image_prompt_en": "",
      "camera": "",
      "dialogue": [
        {
          "speaker": "",
          "text": ""
        }
      ],
      "narration": "",
      "sfx": "",
      "emotion": "",
      "continuity_notes": ""
    }
  ]
}
```

## 6. Prompt Tạo Character Bible

```text
Tạo Character Bible cho nhân vật sau:

Tên: {{character_name}}
Vai trò: {{role}}
Mô tả truyện: {{character_description}}

Yêu cầu:
- Thiết kế nhân vật đủ nhất quán để gen ảnh nhiều lần.
- Có mô tả khuôn mặt, tóc, trang phục, khí chất, màu chủ đạo, đạo cụ.
- Có trạng thái thường ngày, chiến đấu, trọng thương, đột phá cảnh giới.
- Tạo prompt ảnh tiếng Anh cho từng trạng thái.

Trả về JSON:
{
  "name": "",
  "role": "",
  "core_visual_identity": "",
  "face": "",
  "hair": "",
  "outfit": "",
  "color_palette": [],
  "signature_props": [],
  "states": [
    {
      "state": "normal",
      "description_vi": "",
      "image_prompt_en": ""
    }
  ],
  "negative_prompt": "text, watermark, logo, extra fingers, deformed hands, distorted face, duplicate character"
}
```

## 7. Prompt Tạo Prompt Ảnh Panel

```text
Viết prompt ảnh cho panel webtoon sau:

Panel:
{{panel_json}}

Character Bible:
{{character_bible}}

Style:
{{art_style}}

Yêu cầu:
- Prompt bằng tiếng Anh.
- Không có chữ, caption, speech bubble trong ảnh.
- Mô tả rõ nhân vật, trang phục, bối cảnh, ánh sáng, camera, mood.
- Giữ style nhất quán.
- Thêm negative prompt.

Trả về:
{
  "positive_prompt": "",
  "negative_prompt": ""
}
```

## 8. Prompt Chuyển Webtoon Thành Video Short

```text
Chuyển các panel webtoon sau thành kịch bản video short 60-90 giây:

{{panels_json}}

Yêu cầu:
- Tạo timeline theo giây.
- Mỗi đoạn dùng panel nào, hiệu ứng camera nào, narration nào, SFX nào.
- Ưu tiên motion comic: zoom, pan, parallax, shake, glow, particle.
- Kết video bằng cliffhanger và CTA ngắn.

Trả về JSON:
{
  "duration_seconds": 75,
  "timeline": [
    {
      "start": 0,
      "end": 5,
      "panel_id": 1,
      "motion": "slow zoom in",
      "narration": "",
      "dialogue": "",
      "sfx": "",
      "music_mood": ""
    }
  ],
  "title_hook": "",
  "ending_cliffhanger": "",
  "cta": ""
}
```

## 9. Prompt Tạo Video AI Từng Cảnh

```text
Tạo prompt video AI cho cảnh tu tiên sau:

Cảnh:
{{scene_description}}

Nhân vật:
{{character_bible}}

Bối cảnh:
{{location_bible}}

Yêu cầu:
- Prompt bằng tiếng Anh.
- Mô tả shot type, subject, motion, camera, lighting, atmosphere.
- Không dùng nhân vật có bản quyền.
- Không yêu cầu chữ trong video.
- Dài 5-8 giây, cinematic xianxia fantasy.

Trả về JSON:
{
  "video_prompt_en": "",
  "duration_seconds": 5,
  "aspect_ratio": "9:16",
  "camera_motion": "",
  "negative_prompt": "text, logo, watermark, distorted face, extra limbs, bad hands"
}
```

## 10. Prompt Kiểm Tra Chất Lượng

```text
Bạn là editor khó tính của Tu Tien AI Studio.

Hãy review nội dung sau:
{{content}}

Chấm điểm 1-10 theo các tiêu chí:
- Độ hấp dẫn.
- Logic tu tiên.
- Nhất quán nhân vật.
- Khả năng chuyển thành webtoon/video.
- Độ khác biệt so với truyện tu tiên phổ biến.

Sau đó đề xuất bản sửa cụ thể.

Trả về JSON:
{
  "scores": {
    "hook": 0,
    "cultivation_logic": 0,
    "character_consistency": 0,
    "visual_adaptability": 0,
    "originality": 0
  },
  "problems": [],
  "fixes": [],
  "rewrite_suggestion": ""
}
```

## 11. Workflow MVP Khuyến Nghị

```text
1. Người dùng nhập ý tưởng.
2. Generate Story Bible.
3. Generate Character Bible cho nhân vật chính/phản diện.
4. Generate outline 30 chương đầu.
5. Generate chương 1.
6. Convert chương 1 thành 20-30 panel webtoon.
7. Generate ảnh 5 panel quan trọng trước để test style.
8. Dàn trang webtoon.
9. Convert 5 panel thành video short 30-60 giây.
10. Đăng TikTok/YouTube Shorts để đo phản ứng.
```

## 12. Biến Prompt Dùng Trong App

```text
{{idea}} - Ý tưởng ban đầu của người dùng
{{tone}} - Tông giọng: dark, epic, hài, báo thù, trưởng thành
{{audience}} - Đối tượng đọc
{{chapter_count}} - Số chương
{{word_count}} - Số chữ mỗi chương
{{story_bible}} - JSON thế giới và luật truyện
{{character_bible}} - JSON nhân vật
{{location_bible}} - JSON bối cảnh
{{chapter_outline}} - Outline chương
{{continuity_state}} - Trạng thái continuity hiện tại
{{chapter_text}} - Nội dung chương
{{panels_json}} - Danh sách panel webtoon
{{art_style}} - Phong cách ảnh
```

## 13. Style Preset Gợi Ý

```text
Anime webtoon xianxia, cinematic lighting, elegant character design, flowing robes, glowing spiritual energy, dramatic clouds, high detail, clean line art, vertical comic composition
```

```text
Dark cultivation fantasy, ink wash atmosphere, cold moonlight, ancient sect ruins, sharp contrast, mystical talismans, cinematic composition, detailed webtoon panel
```

```text
Epic immortal cultivation fantasy, golden divine aura, floating mountains, sword flight, storm clouds, majestic scale, dynamic camera angle, polished anime illustration
```

