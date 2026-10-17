---
name: soat-ux-bang-ui-ux-pro-max
description: "Soát UX bằng ui-ux-pro-max trước khi ghi giao diện — Sáng hỏi \"em không xài ux ui pro max à\" sau hai lần chê một thẻ giao diện (12/10/2026)"
---

> Nguồn: ghi nhớ `soat-ux-bang-ui-ux-pro-max`. Đã lược phần riêng dự án; bản này sửa trực tiếp trong repo.

Skill **ui-ux-pro-max** cài toàn cục ở `C:\Users\Admin\.claude\skills\ui-ux-pro-max\` (bản 2.15.0 từ 18/10/2026; bản gốc lưu ở
`vendor/ui-ux-pro-max-skill` của repo này). Gọi bằng Skill `ui-ux-pro-max`. Câu lệnh tra:
`python "C:/Users/Admin/.claude/skills/ui-ux-pro-max/scripts/search.py" "<từ khoá>" --domain ux -n 5`
(chạy được cả PowerShell lẫn Bash, không cần đặt biến mã hoá).

- **Cách cài:** làm tay giống `uipro init --ai claude --global` — `scripts/install.ps1` của repo đã làm sẵn:
  - chép `skills/ui-ux-pro-max`, bỏ `__pycache__`;
  - đổi 11 chỗ `${CLAUDE_PLUGIN_ROOT}/.claude/skills/...` sang đường dẫn tuyệt đối. KHÔNG dùng `~` vì PowerShell 5.1 không mở `~` cho python;
  - `SKILL.md` gốc xuống dòng kiểu CRLF; thay chuỗi theo `\n` sẽ trượt.
- **Cập nhật:** `python scripts/sync.py` kéo bản mới của repo gốc về `vendor/`, rồi `scripts/install.ps1 -Force`.
- **Phạm vi:** skill viết cho web/mobile/desktop; giao diện ngoài các stack đó chỉ lấy phần luật UX và `references/pro-rules.md` (checklist).

**Why:** 12/10/2026 một thẻ giao diện bị chê hai lần ("xấu vãi", "vẫn thấy xấu"). Sáng hỏi "em không xài ux ui pro max à".
Soát bằng skill bắt được bốn lỗi em không tự thấy:
- chữ xám `#9AA0A8` trên nền trắng chỉ 2,6:1 (cần 4,5:1); chữ xanh `#339966` chỉ 3,6:1;
- trạng thái chỉ phân biệt bằng màu;
- hai ô chọn dính nhau (cần cách ít nhất 8 px);
- ô bị khoá khi đang chạy vẫn trông như bấm được.

**How to apply:** Trước khi ghi một giao diện vào project, chạy `search --domain ux` cho các chủ đề: contrast, color only,
touch target/spacing, disabled state. Tính tương phản từng cặp màu chữ/nền. Nói ngắn cho Sáng skill bắt được gì và đã sửa gì.
Màu vẫn lấy theo bộ mặt có sẵn của sản phẩm đang làm, không lập bảng màu mới chỉ vì soát UX.
Web/app thì vẫn đi [frontend-design-truoc](frontend-design-truoc.md) trước.
