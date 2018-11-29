# PwLaunch

An Ableton Live 10 remote script to be used with a Novation Launchpad mk2

## Development

[Contribution Guide](https://github.com/pineapplemidi/pwlaunch/blob/master/CONTRIBUTING.md)

_This assumes one knows how to add a remote script to the ableton live remote
scripts directory_

Create a file named `config.json` in the home directory. Put the following
contents in it:

```json
{
  "width": 1,
  "height": 1
}
```

Replace `PwLaunch.py:33` with the correct path to you home directory. The line
is as follows: `/users/berry/config.json`

Replace `PyLaunch.py:46` with the correct path to your home directory. The line
is as follows: `/users/berry/pwlaunch.txt`

To see the logs, open a terminal window an return

```bash
$ tail -f pwlaunch.txt
```

## Documentation

### v0.0.0

![v0.0.0](./docs/imgs/PwLaunch-0.0.0.png)

## Resources

+ [Unofficial API docs](https://julienbayle.studio/PythonLiveAPI_documentation/Live10.0.2.xml)
+ [Remote script repos](https://github.com/gluon/AbletonLive10_MIDIRemoteScripts)
