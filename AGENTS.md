# Hướng dẫn cho agent

Repo này là bộ skill tài liệu và thiết kế của Sáng (Office, PDF, Adobe, UI/UX).

- Việc nào cũng bắt đầu ở `skills/office-design/SKILL.md`; nó chỉ sang đúng skill.
- Chỉ mở `references/*.md` qua bảng trong `SKILL.md` của chính skill đó.
- `references/*.md` có dòng "Chép tự động bằng `scripts/sync.py`" — **đừng sửa trong repo**; sửa ghi nhớ gốc rồi chạy `python scripts/sync.py`.
  Dòng "Đã lược phần riêng dự án" thì sửa thẳng trong repo.
- Mọi thứ trong `vendor/` là bản chép của bên thứ ba; cập nhật bằng `sync.py`, không sửa tay.
- Thêm ghi chú: thêm dòng vào `scripts/sources.tsv`; thêm skill: tạo `skills/<tên>/SKILL.md` (frontmatter `name` trùng tên thư mục),
  cập nhật bảng trong `README.md` và `skills/office-design/SKILL.md`, rồi chạy `python scripts/check_repo.py`.
- Không đưa vào repo: tên dự án riêng, skill `docx`/`xlsx`/`pptx`/`pdf` của Anthropic, token, mật khẩu, đường dẫn phần mềm cài trên máy,
  file khách hàng (`.docx`, `.xlsx`, `.ai`, `.psd` thật). `check_repo.py` soát từ cấm theo `scripts/tu-cam.local.txt` (chỉ có trên máy Sáng).
- Script `.ps1` giữ thuần ASCII (PowerShell 5.1); chữ Việt để trong `.md`/`.py`/`.json` UTF-8.
