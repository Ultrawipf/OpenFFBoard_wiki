## Firmware Development

The Firmware-Git can be found here: [OpenffBoard-Firmware](https://github.com/Ultrawipf/OpenFFBoard).

At the moment the STM IDE is used to compile the code and upload it to your OpenFFBoard. The IDE can be downloaded here: [IDE](https://www.st.com/en/development-tools/stm32cubeide.html#get-software).

### Git workflow
Changes should be added in the CHANGELOG.md file.
This will be used to generate release notes.
A tagged commit (v1.x.x) will trigger an automatic release. A tag with a "-" (v1.x.x-beta) generates a prerelease.