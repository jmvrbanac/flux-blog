Title: A software engineer’s perspective on TypeScript
Date: 2012-11-5
Modified: 2014-11-09 11:44
Tags: Cross-Platform, Languages, Software Engineering, TypeScript
Slug: software-engineers-perspective-on-typescript
Authors: John Vrbanac

For those who have been keeping up with the latest news in the web
development world, you’ve probably seen the introduction of TypeScript.
I have heard the perspectives of many other people on this new language,
but I wanted to actually work with language a bit before I started
deriving my opinion. Given that I have worked with it for a few of weeks
now, I think it’s about time I put something in writing.

Before I talk about TypeScript, let’s get one thing out of the way,
attempting to develop large-scale applications with maintainable and
testable code in JavaScript is horrific. Note, I did not say that it was
impossible. If you disagree, then I would highly suggest you read a couple
software engineering books such as [The Art of Readable code by Boswell and Foucher](http://www.amazon.com/gp/product/0596802293/ref=as_li_ss_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=0596802293&linkCode=as2&tag=vertdesi-20)
, or [The Pragmatic Programmer by Andrew Hunt](http://www.amazon.com/gp/product/020161622X/ref=as_li_ss_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=020161622X&linkCode=as2&tag=vertdesi-20)
. If you still disagree after reading those books, work a while on larger
scale projects using C++, Java, C#, Python, or some other more traditional
language. If you still “don’t see the light,” I’m sorry, there is probably
no hope for you and you might as well stop reading now.

What is TypeScript?
--------------------

TypeScript is an open-source superset of JavaScript. In essence, its
creators acknowledge that people aren’t going to get rid of JavaScript
anytime soon, but people still need to create large-scale maintainable
applications in JavaScript. As a result, the authors of TypeScript decided
to expand JavaScript to make it faster to develop, easier to maintain,
quicker to debug, faster to tool, and make the development experience better
for large-scale app development. TypeScript uses a compiler to handle
modules, classes, type inference, and module dependencies; all of which help
accomplish some of the goals mentioned.

Who is the publicly visible team that has developed TypeScript?
----------------------------------------------------------------

Generally speaking, a language can live or die based on the architects of
the language. As a result, it is important to know who is behind it and how
likely are they to continue their efforts. From what we are told, the
primary visible team contains Steve Lucco, Anders Hejlsberg, Erich Gamma,
and Luke Hoban. If you are a professional software engineer, at least two
of those names should mean something to you and should give you some
confidence in the design, direction, and possible lifespan of the language.

Pros & Cons
------------

**Pros**

* Open Source
* Compile-time syntax and type (if types are specified) checking.
* Allows for OO paradigms to be utilized in development. This is very
important for full-scale application development.
* Type inference. Takes advantage of the dynamic typing that JS provides,
but allows for some structure around it if desired. Allows for intellisense
like completion when used.
* Generates JS output in ES3 and ES5 for better back compatibility.
* Allows the usage of pure JS libraries through definition files. That
means that you don’t have to port every library you want to use.
* Takes the pain out of AMD (such as Require.JS) or CommonJS module loading.
* Simplifies continuous integration substantially. I was able to put
together a full [Jenkins CI TypeScript project](https://github.com/jmvrbanac/TypeScript-CI-Starter)
using Node, Gradle, Jasmine, and Require.JS in a very short time. I’ll talk
about that some other time, but for now I have pushed up a copy of that
project to my [GitHub](https://github.com/jmvrbanac/TypeScript-CI-Starter)
for you to check out.

**Cons**

* As with any language that compiles to another, there is always a
disconnect between the code that is written and the code that is generated.
To remedy this, it appears that TypeScript attempts to leave as much of the
pure JS that is written within functions alone. From my experience, it pretty
much copies it verbatim.
* External and Internal module loading isn’t documented really well and
can be a bit of a pain to figure out for complex module structures.
* Only a few definition files are available right now as the language is
so new. However, this is changing through the DefinitelyTyped community project.
* Tutorials and documentation are a bit scarce due to the age of the language.
* Autocompletion is only available in VS2012 and syntax highlighting is only
available in a select few editors. While I expect for this to change, it
is the reality when this post was written.
* The language is still in “preview”

Opinion
--------

I personally believe that TypeScript even in its current “preview” form
allows for faster, easier, and better development for the current web
development situation. While I have only written about 1000 or so lines of
it at this point, I can definitely state for the record that it’s a breath of
fresh air to the aged and stagnate conglomeration that is JavaScript. Coming
from someone who has worked with many languages, one of the most important
things I look for in a good language is being able to utilize language
agnostic skills, concepts, and techniques within a given language. I know
many web developer’s diss the need for traditional OOP concepts that
TypeScript brings. However, I would argue that it is a very important
requirement for full-stack or traditional developers.

Outside of all of the other things that TypeScript brings, probably one of
the most important pieces is the compile-time checking. Sure JavaScript
has JSHint and JSLint, but anyone who has used those knows that they only
catches the basics. TypeScript on the other hand will tell you the full
story. A simple example is if you try to assign a string to a variable
that is currently a number. TypeScript would throw an error due to mixed
assignment. While this may seem trivial, such a simple check can save you
valuable debug time. The idea is to allow the compiler to do the hard work
for you during development time.

As a side note, It is also my personal opinion that anyone who complains
about TypeScript bringing structure, type inference, more traditional OO
paradigms, and Lambda functions to JavaScript should take a hard look at
what they know. In my mind, any professional software engineer should
understand the importance of structure and why traditional OO paradigms
are necessary for developing large-scale maintainable applications.
It’s not that to say that you can’t develop large scale apps without it,
but rather it is horrible to do so and for your own sanity you shouldn’t.

Recommendation
----------------

I highly recommend TypeScript. Even though it is currently out as a
preview, I believe that the core concepts are solid and probably won’t
change too much. It scratches an itch that has gone unscratched for
many years until now. It acts as a bridge technology so that older
browsers aren’t left behind while still being compatible with the
plethora of JavaScript libraries in existence. I hope you will spend
some time with it and see what I’m talking about first hand. Hop on
over to the [TypeScript website](http://www.typescriptlang.org/) and
give it a shot.