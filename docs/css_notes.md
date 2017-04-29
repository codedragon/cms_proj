#CSS Notes

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

