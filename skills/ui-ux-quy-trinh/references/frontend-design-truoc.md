---
name: thiet-ke-ui-dung-skill-frontend-design
description: "Sáng muốn mọi việc thiết kế giao diện (web, artifact, app desktop) đi qua skill frontend-design của Anthropic trước khi viết code"
---

> Nguồn: ghi nhớ `thiet-ke-ui-dung-skill-frontend-design`, cập nhật 2026-09-19. Đã lược phần riêng dự án; bản này sửa trực tiếp trong repo.

Ngày 19/09/2026 Sáng cài plugin `frontend-design@claude-plugins-official` (skill chính chủ Anthropic,
cùng nội dung với `plugins/frontend-design/skills/frontend-design/SKILL.md` trong repo claude-code)
và yêu cầu: **khi thiết kế giao diện thì để skill này dẫn dắt**, không tự vẽ theo thói quen.
Luật đã ghi ở `~/.claude/CLAUDE.md`.

**Why:** Sáng không muốn UI ra kiểu "AI sinh" nhìn giống nhau (nền kem + serif + màu đất nung,
card bo góc bóng xám, nhãn ALL-CAPS, mũi tên → trên nút). Skill ép lập token màu/chữ/bố cục
theo đúng chủ đề rồi tự soát trước khi code.

**How to apply:**
- Bất kỳ yêu cầu dựng/sửa/làm đẹp UI (web, HTML artifact, app desktop như ORDINO, dashboard,
  form): gọi `Skill frontend-design` **trước dòng code đầu tiên**, lập bảng token 4–6 màu hex +
  font + wireframe ASCII, soát với 5 kiểu mặc định, rồi mới code. Code xong bỏ bớt một trang trí.
- Nói rõ chủ đề và người dùng (thợ vận hành, kỹ sư…) để skill chọn tông công nghiệp, không phải
  landing page.
- Bộ token mẫu có sẵn nếu cần: `awesome-claude-design` (DESIGN.md) trên GitHub — bổ trợ, chưa kéo về.
- Skill `frontend-design-review` (bộ khác, thiên về review) không phải cái này.
