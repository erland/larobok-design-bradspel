-- Anpassa lärobokens H1-rubriker till kompakta kapitelstarter.
function Header(el)
  if el.level ~= 1 then return nil end
  local text = pandoc.utils.stringify(el.content)
  if text:match("^%s*Inledning%s*$" ) then
    return pandoc.RawBlock("latex", "\\bookintro{Inledning}")
  end
  local number, title = text:match("^%s*Kapitel%s+(%d+)%s*:%s*(.-)%s*$")
  if not number then return nil end
  local title_tex = pandoc.write(pandoc.Pandoc({pandoc.Para(pandoc.read(title,"markdown").blocks[1].content)}),"latex"):gsub("%s+$","")
  return pandoc.RawBlock("latex", "\\bookchapter{" .. number .. "}{" .. title_tex .. "}")
end
