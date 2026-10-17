---
name: bash-heredoc-nuot-dau-gach-nguoc
description: "Trong Claude Code trên máy Sáng, lệnh Bash có heredoc/python -c làm mất hoặc biến đổi dấu \\ (\\\\ thành \\, \\b thành backspace, \\11 thành tab) — file có dấu \\ thì viết bằng công cụ Write"
---

> Nguồn: ghi nhớ `bash-heredoc-nuot-dau-gach-nguoc`, cập nhật 2026-10-10. Đã lược phần riêng dự án; bản này sửa trực tiếp trong repo.

10/10/2026 dính 4 lần trong một buổi: `python - <<'PYEOF'` có `r'\\b_stem\\b'` ghi ra file thành ký tự backspace (0x08);
`@"\\14.Ban_2609_v2\\11..."` thành tab + form feed (script tự dừng ở bước kiểm đường dẫn, may không ghi sai); `sed 's#step_lazy\\mod\\base#...#'`
không khớp nên lệnh xuất module ghi đè `step_lazy\mod\base`.

**Why:** dấu `\` bị xử lý trước khi tới Python/sed, kể cả trong heredoc có nháy. Lỗi im lặng: script vẫn chạy, chỉ sai kết quả.

**How to apply:** đoạn mã có `\` (regex, đường dẫn Windows, chuỗi C#) thì viết ra file bằng công cụ **Write** rồi chạy file; trong
`python -c` dùng `chr(92)`. Sau khi sinh file, soi lại dòng có `\` (`od -c` nếu nghi). Liên quan [csc-can-bom-cho-tieng-viet](bom-tieng-viet.md).
