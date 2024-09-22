# Markdown Markup Language


# HEADERS

```
# H1
## H2
### H3
#### H4
##### H5
###### H6
```
# LISTS
```
1. First ordered list item
2. Another item
  * Unordered sub-list. 
1. Actual numbers don't matter, just that it's a number
  1. Ordered sub-list
4. And another item.  
   
   Some text that should be aligned with the above item.

* Unordered list can use asterisks
- Or minuses
+ Or pluses
```
# LINKS

```
[I'm an inline-style link](https://www.google.com)

[I'm a reference-style link][Arbitrary case-insensitive reference text]

[You can use numbers for reference-style link definitions][1]

Or leave it empty and use the [link text itself]
```
# IMAGES
```
<picture> 
<img alt = "logo" src = "logoPense.png">
</picture>
```
# CODE AND SYNTAX HIGHLIGHTING
 Code blocks are part of the Markdown spec, but syntax highlighting isn't. However, many renderers -- like Github's and Markdown Here -- support syntax highlighting. Markdown Here supports highlighting for dozens of languages 
```
 ```python
s = "Python syntax highlighting"
      print s
```
 
```
 ```
No language indicated, so no syntax highlighting. 
But let's throw in a <b>tag</b>.
 ```
```

# TABLES
You can also make tables but I won't show it here because I don't think I will be using it.
NOTE:The first thing in the morning after I wrote that I dOnT tHinK i'LL uSe iT, I needed it 
Colons can be used to align columns.

| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |

There must be at least 3 dashes separating each header cell.
The outer pipes (|) are optional, and you don't need to make the 
raw Markdown line up prettily. You can also use inline Markdown.

Markdown | Less | Pretty
--- | --- | ---
*Still* | `renders` | **nicely**
1 | 2 | 3

# BLOCKQUOTES

You can use quotes with markdown. just use the > sign in the beginning of the line
```
> like this
```

# INLINE HTML

You can use HTML tags with markdown. Nearly every tag works with MD.
```
<dl>
  <dt>Definition list</dt>
  <dd>Is something people use sometimes.</dd>

  <dt>Markdown in HTML</dt>
  <dd>Does *not* work **very** well. Use HTML <em>tags</em>.</dd>
</dl>
```

