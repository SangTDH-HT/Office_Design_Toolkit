# Bên thứ ba

Repo riêng tư của Sáng. Phần tự viết (`skills/`, `scripts/`, `assets/`, `docs/`, `mcp/`) không cấp phép cho người ngoài.
Các thành phần dưới đây giữ nguyên giấy phép gốc.

## Có trong repo

| Thư mục | Nguồn | Giấy phép | File giấy phép |
|---|---|---|---|
| `vendor/frontend-design` | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official), plugin `frontend-design` | Apache License 2.0 | `vendor/frontend-design/LICENSE` |
| `vendor/ui-ux-pro-max-skill` | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) v2.15.0, commit `56ea9cf` | MIT | `vendor/ui-ux-pro-max-skill/LICENSE` |
| `vendor/ui-ux-pro-max-skill/skills/ui-styling` | như trên; phần canvas-design gốc Apache 2.0, font trong `canvas-fonts/` theo SIL Open Font License | Apache 2.0 / OFL 1.1 | `ui-styling/LICENSE.txt`, `canvas-fonts/*-OFL.txt` |

## Không có trong repo (chỉ dặn cách cài)

| Thành phần | Lý do |
|---|---|
| Skill `docx`, `xlsx`, `pptx`, `pdf` của Anthropic | Giấy phép cấm sao chép và phân phối; có sẵn trong Claude |
| Plugin `ppt-master` ([hugohe3/ppt-master](https://github.com/hugohe3/ppt-master), MIT) | 107 MB; cài bằng `/plugin` |
| `illustrator-mcp-server` (ie3jp, MIT) | `npx -y` tự tải |
| `illustrator-mcp` (krVatsal), `@alisaitteke/photoshop-mcp` | Cài theo `mcp/README.md` |
