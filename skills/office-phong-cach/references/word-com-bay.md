---
name: word-com-docx-gotchas
description: "Word COM automation gotchas hit on the graduation report .docx (Google Docs export)"
---

> Nguồn: ghi nhớ `word-com-docx-gotchas`, cập nhật 2026-08-12. Chép tự động bằng `scripts/sync.py` — sửa ở ghi nhớ gốc rồi chạy lại.

Editing the user's .docx files is done through Word COM from PowerShell (no python/python-docx, no PDF renderer on this machine — verify layout by unzipping the .docx and reading the XML, not by screenshotting Word: `SetForegroundWindow` loses the race and captures VS Code instead).

Three things that cost round trips on `Downloads\Báo cáo tốt nghiệp.docx`:

- **Google Docs exports set the `Normal` style to `outlineLvl = 0`**, so every ordinary paragraph counts as Heading 1 and a TOC field swallows the whole document. Fix: `$doc.Styles.Item(-1).ParagraphFormat.OutlineLevel = 10` (wdOutlineLevelBodyText) before inserting `TOC \o "1-3" \h`.
- **Tab dot-leaders do not render for a trailing tab** — fill-in lines must be literal `.` characters (130 dots ≈ one 6" line at 13pt Times) or a dotted bottom border.
- **`PageSetup.DifferentFirstPageHeaderFooter` silently reverts** if set before the header/footer content is written; set it last and re-read the value (`w:titlePg` must appear in the saved sectPr).

- **`$doc.Paragraphs.Item($i)` inside a loop is O(n²)** — Word re-walks the story each call. On a 1000-paragraph file a 5-anchor search hung for 30+ minutes; enumerating once (`foreach ($p in $doc.Paragraphs)`) and keeping the paragraph objects took 5 seconds. Same for `Tables.Item()`/`InlineShapes.Item()` in loops.
- **Tables inherit the heading style at the insertion point** — a table created after a Heading 2 puts every cell in the TOC; set `$tbl.Range.Style = Normal` (setting OutlineLevel alone is not enough, `TOC \o` matches by style).
- **Images in `DATN_FPL.docx` are broken links** (they render as `/`), so `FormattedText` copies produce an empty paragraph plus a caption. After copying, delete captions whose preceding paragraph has no InlineShape.

New paragraphs inherit the previous paragraph's borders/colour/letter-spacing, so clear `Borders`, `Font.Color` and `Font.Spacing` on appended ranges. See [ps51-utf8-script-encoding](ps51-utf8-tieng-viet.md) — keep the .ps1 ASCII and load Vietnamese strings from UTF-8 .txt files.

## Cat bot muc bang cach sua document.xml

Khi phai xoa hang tram doan (trich mot phan bao cao ra file rieng), sua thang `word/document.xml` bang `ElementTree` nhanh hon COM hang tram lan: duyet con cua `w:body`, tim doan co `w:pStyle` = Heading*, moi tieu de mo mot khoi keo dai toi tieu de ke tiep, roi xoa tu duoi len. Doi ten/doi cap tieu de **truoc khi xoa** de chi so con dung.

Hai cai bay bat buoc phai biet:

- **ElementTree keo xmlns len root** — cac prefix `a`, `a14`, `pic` trong file goc duoc khai bao ngay tren `<a:graphic>`/`<pic:pic>`, ET gom het len the `<w:document>` cua no. Neu ghi de the root bang the goc (de giu `mc:Ignorable`) thi ba prefix do thanh **unbound** va Word bao "The file appears to be corrupted". Phai **hop nhat**: lay the goc roi bo sung nhung `xmlns:` nao ET co ma the goc khong co.
- **Doan trong nam trong ket qua field TOC** khong xoa duoc (`Cannot edit Range`). Muon bo trang trang thua sau muc luc thi ha co chu xuong 1 pt, dung tim cach xoa.

Doan mau va tieu de moi nen `deepcopy` tu mot doan **that trong than bai** (`pStyle` rong, co `w:r` truc tiep). Copy nham mot dong muc luc la dinh: runs cua no nam trong `w:hyperlink` nen `p.findall(w:r)` rong, chu moi bi noi vao duoi chu cu.
