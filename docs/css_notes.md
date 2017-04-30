# CSS Notes

### Difference between div id and div class

http://stackoverflow.com/questions/544010/difference-between-div-id-and-div-class

ids must be unique where as class can be applied to many things. In CSS, ids look like #elementID and class elements look like .someClass

In general, use id whenever you want to refer to a specific element and class when you have a number of things that are all alike. For instance, common id elements are things like header, footer, sidebar. Common class elements are things like highlight or external-link.

It's a good idea to read up on the cascade and understand the precedence assigned to various selectors: http://www.w3.org/TR/CSS2/cascade.html

The most basic precedence you should understand, however, is that id selectors take precedence over class selectors. If you had this:

`<p id="intro" class="foo">Hello!</p>`

and:

```
#intro { color: red }
.foo { color: blue }
```

The text would be red because the id selector takes precedence over the class selector.





I know that in a stylesheet div#name and #name do the same thing. Personally I've taken to using div#name for most styling I do, with the reasoning that it's slightly faster, and means that I can identify HTML elements more easily by looking at the CSS.

However all of the big websites I seem to look at use #name over div#name (stack overflow included)

In fact I'm finding it very difficult to find many websites at all that use div#name over #name

Is there some advantage to doing #name that I'm missing? Are there any reasons to use it over div#name that I don't yet know about?
