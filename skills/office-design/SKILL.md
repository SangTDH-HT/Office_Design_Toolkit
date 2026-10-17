---
name: office-design
description: Cửa vào bộ skill tài liệu và thiết kế của Sáng — chọn đúng skill cho Word/Excel/PowerPoint, PDF dựng từ HTML, hướng dẫn sử dụng, sơ đồ draw.io, Adobe Illustrator/Photoshop, thiết kế UI/UX (web, artifact, dashboard, app WPF). Dùng khi Sáng nhờ "làm tài liệu", "soạn file Word", "xuất PDF", "làm hướng dẫn", "vẽ sơ đồ", "làm slide", "mở Illustrator/Photoshop", "thiết kế giao diện", "làm đẹp", "căn chỉnh", "phong cách như cũ" mà chưa rõ đi đường nào.
---

# Cửa vào: tài liệu và thiết kế

Đọc bảng, mở đúng skill, rồi làm theo skill đó. Mỗi skill tự trỏ tới `references/` của nó.

## Chọn skill

| Việc | Skill |
|---|---|
| Sửa/dựng `.docx`, form KHBD, báo cáo có mục lục và chú thích hình; bảng tính `.xlsx`; slide `.pptx`; script COM tiếng Việt | [office-phong-cach](../office-phong-cach/SKILL.md) |
| PDF đẹp dựng từ HTML (Chrome/Edge headless), tài liệu vận hành, hướng dẫn có ảnh khoanh vùng, bài làm để chép, tài liệu ôn thi, đề xuất có đồ thị, sơ đồ draw.io | [tai-lieu-pdf](../tai-lieu-pdf/SKILL.md) |
| Illustrator, Photoshop, file `.ai`/`.psd`/`.jsx`, banner, bìa, xoá nền ảnh | [adobe-phong-cach](../adobe-phong-cach/SKILL.md) → [illustrator](../illustrator/SKILL.md) |
| Giao diện web, HTML artifact, dashboard, form, app desktop WPF | [ui-ux-quy-trinh](../ui-ux-quy-trinh/SKILL.md) |

Skill có sẵn trong Claude, repo này không chép (bản quyền hoặc quá nặng), chỉ dặn cách dùng:
`docx`, `xlsx`, `pptx`, `pdf` (Anthropic), `dataviz`, `artifact-design`, `ppt-master` (plugin), `frontend-design` (plugin, có bản lưu ở `vendor/`), `ui-ux-pro-max` (cài toàn cục, bản lưu ở `vendor/`).

## Luật chung cho mọi tài liệu

1. **Hỏi người đọc trước khi dựng.** Thợ vận hành, khách, giáo viên, quản lý hay chính Sáng — mỗi người một khuôn. Tài liệu cho thợ/Sáng: ít chữ, không tên biến, không mã nguồn, sơ đồ thay đoạn văn.
2. **Sửa bản sao, không tắt app của Sáng.** File Office bị khoá → báo tiến trình nào giữ và xin phép; sửa bản sao trong scratchpad rồi chép đè. Bản cũ giữ bằng hậu tố `.bak-before-<việc>` hoặc `- ban goc.docx` cạnh file.
3. **Nhìn bằng mắt trước khi báo xong.** Render trang ra PNG (PyMuPDF, draw.io CLI, Chrome headless, Illustrator xuất PNG) rồi đọc ảnh. Log không báo chữ tràn, chữ chồng, mất dấu.
4. **Tiếng Việt đủ dấu ở mọi khâu.** Font có glyph Việt (Times New Roman, Arial, Segoe UI, Be Vietnam Pro; không Arial Black, không subset Google Fonts); script có chữ Việt thì đúng BOM/encoding.
5. **Đặt tên và chỗ để theo quy ước của Sáng**: `<số>.<Ten_Khong_Dau>.pdf`, nguồn `.html` cùng tên đặt cạnh (chi tiết ở `tai-lieu-pdf`). Không thả file lạ ra gốc dự án.
6. **"Biên soạn: Nguyễn Hữu Sáng"** chỉ ghi khi Sáng bảo ghi tên người biên soạn/tác giả.
7. **Giao diện nào cũng qua `frontend-design` trước dòng code đầu** — chi tiết ở `ui-ux-quy-trinh`.
8. Tin nhắn soạn hộ Sáng: 1–2 câu tự nhiên, không khen, tối đa một emoji.
