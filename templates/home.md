Welcome!

The WL ModCabinet wiki exists to provide a slightly-easier way of browsing through
the Wonderlands mods hosted on the
[wlmods Github](https://github.com/BLCM/wlmods) -- all nicely arranged in
categories rather than just organized by author.  

This wiki is a resource for users who are just looking to run some mods.
For information on actually building your own mods, the [BLCMods
Wiki](https://github.com/BLCM/BLCMods/wiki/Wonderlands-Modding-Info) is your best
starting point.

# Mod Categories

{%- for cat in categories %}
{%- if cat.prefix and (not loop.previtem or not loop.previtem.prefix or (loop.previtem.prefix != cat.prefix)) %}
- {{ cat.prefix }}
{%- endif %}
{%- if cat.prefix %}
  - {{ cat.wiki_link() }}
{%- else %}
- {{ cat.wiki_link() }}
{%- endif %}
{%- endfor %}

# Other Pages

- [[Authors]]
- [[About WL ModCabinet Wiki]]
- [[Contributing to WL ModCabinet]]
- [[Searching on the Wiki|Searching]]
