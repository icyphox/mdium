# mdium
> publish your markdown to Medium, from the CLI

## Installation

```console
$ pip install mdium
```


## Usage

### Initializing

First off, set up `mdium` with your Medium integration token. You’ll have to generate one from the [settings](https://medium.com/me/settings) page.
```console
$ mdium init <integration-token>
```

This will create a file at `~/.mdium`, containing your integration token and author ID.

### Publishing

For publishing, your markdown doc must have the following frontmatter:

```yaml
---
title: My Awesome Post
tags: ['some', 'tags', 'here']
status: draft
---

## markdown here
...
```

Note that the `status` field can be either `draft` or `public`.

Finally, run

```console
$ mdium publish path/to/markdown.md
Done! Your post has been published at https://medium.com/@gaben/76272e9d241c
```

It’s that simple.

## License

MIT © Anirudh Oppiliappan
