---
name: ask-before-killing-user-apps
description: "Hỏi trước khi Stop-Process các app của người dùng (Word/Excel), kể cả khi chúng đang giữ khóa file"
---

> Nguồn: ghi nhớ `ask-before-killing-user-apps`, cập nhật 2026-08-13. Chép tự động bằng `scripts/sync.py` — sửa ở ghi nhớ gốc rồi chạy lại.

Ngày 2026-08-13, khi script Word COM treo vì file `.docx` bị khóa, tôi đã `Stop-Process -Force` toàn bộ `WINWORD.EXE` mà không hỏi. Người dùng đang mở file đó và hỏi lại "sao tắt word rồi".

**Why:** tắt app của người dùng có thể làm mất nội dung chưa lưu — đó là hành động khó đảo ngược, thuộc quyền quyết định của họ, không phải của tôi.

**How to apply:** khi file Office bị khóa, trước hết báo cho người dùng biết tiến trình nào đang giữ và xin phép đóng. Đồng thời giảm nhu cầu phải tắt: **sửa trên bản sao trong scratchpad rồi mới `Copy-Item` đè lên bản gốc** — cách này chạy được cả khi bản gốc đang mở, và giữ nguyên file gốc nếu Word chết giữa chừng. Chỉ dọn tiến trình mồ côi do chính mình tạo ra (Word `Visible=$false` còn sót vì script lỗi) sau khi đã xác nhận không phải cửa sổ của người dùng. Kiểm tra `%APPDATA%\Microsoft\Word` và `%LOCALAPPDATA%\Microsoft\Office\UnsavedFiles` để biết có dữ liệu AutoRecover hay không.

Liên quan: [word-com-docx-gotchas](word-com-bay.md), [word-seq-caption-field](word-caption-seq.md).
