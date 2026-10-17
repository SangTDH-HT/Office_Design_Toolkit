---
name: photoshop-mcp
description: "Dùng MCP photoshop (@alisaitteke/photoshop-mcp) trên máy Sáng — thứ tự gọi tool, recipe thay chuỗi thao tác lẻ, xoá nền đúng một recipe"
---

> Viết 18/10/2026 từ hướng dẫn đi kèm MCP `photoshop` đang cài (scope user, `node …\@alisaitteke\photoshop-mcp\dist\index.js`).
> Chưa có bài học riêng của Sáng — thêm vào đây khi gặp.

## Thứ tự gọi

1. `photoshop_ping` **một lần** đầu phiên để biết đã nối được.
2. Trước tính năng AI (Generative Fill, Upscale, Select Subject v2, neural filter): `photoshop_get_capabilities` một lần — bản Photoshop trên máy có thể không có.
3. Trước mọi tool cần tài liệu/layer: `photoshop_get_state`; lấy `document.id` và truyền `document_id` cho tool sửa — tab đang chọn có thể đổi ngoài ý.
4. Mở hơn một tài liệu: `photoshop_list_documents`, ghim `document_id` cả khi xem trước, lưu, đóng.
5. Xem kết quả bằng `photoshop_get_preview` sau mỗi bước lớn (không sau từng thao tác nhỏ).

## Xoá nền (xoá phông, tách chủ thể, nền trong suốt)

`photoshop_get_state` → `photoshop_recipe_remove_background` → `photoshop_get_preview`, rồi dừng.
Recipe tự mở khoá layer Background. Không tự chế bằng rasterize / duplicate / select subject / mask / generative remove.
Recipe báo lỗi thì báo nguyên văn lỗi cho Sáng.

## Ưu tiên recipe

Việc khớp recipe thì dùng recipe thay cho 5+ thao tác lẻ: `recipe_prepare_for_web`, `recipe_export_social_variants`,
`recipe_apply_color_grade`, `recipe_enhance_portrait`, `recipe_frequency_separation`, `recipe_batch_mockup_replace`,
`recipe_organize_layers`, `recipe_sky_blend`, `recipe_gradient_fade`, `recipe_dodge_burn`, `recipe_remove_distraction`,
`recipe_csv_to_cards`, `recipe_batch_watermark`, `recipe_split_carousel`, `recipe_passport_photo`.

## Cài lại

Cấu hình mẫu ở `mcp/photoshop.mcp.json` của repo; điền `PHOTOSHOP_PATH` tới `Photoshop.exe` trên máy.
