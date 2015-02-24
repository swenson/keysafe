# keysafe

Keysafe is a simple tool for encrypting a bunch of files with a
bunch of different people's public keys, and keeping those files up-to-date.
It uses the awesome service, [keybase.io](keybase.io), to fetch
keys, although it calls `gpg` directly for increased speed.

## Use cases

* Shared credentials
* Software licenses
* API keys
* Anything else that you want to share, securely, with multiple people

## Requirements

It should work on Linux, OS X, or any other UNIXy system.
It needs Python, `gpg`, and `curl` installed.

## How to use

Clone the repo, or otherwise copy the `keysafe-update` code in particular.

Create an ACL file, like the sample`acl.json`

```json
{
  "deploy.key": ["swenson", "max", "chris"]
}
```

This says that we will encrypt the file `deploy.key` with the
public keys associated to the [keybase.io](keybase.io) users
`swenson`, `max`, and `chris`.

Now, simply run

```sh
./keysafe-update acl.json
```

It will automatically import their keys from the keybase API
and encrypt the specified files.
The files will have `.encrypted` appended to them, e.g.,
`deploy.key` will be encrypted to `deploy.key.encrypted`.

You can then read the file with `keysafe-read`, or with
a simple `gpg --decrypt deploy.key.encrypted` (for example).

## License

Licensed under the MIT license. See [LICENSE.md](LICENSE.md).
