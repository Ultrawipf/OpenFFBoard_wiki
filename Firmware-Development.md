<div align="center">
    <a href="https://github.com/Ultrawipf/OpenFFBoard">
        <img width="100" height="100" src="img/ffboard_logo.svg">
    </a>
	<br>
	<br>
	<div style="display: flex;">
		<a href="https://discord.gg/gHtnEcP">
            <img src="https://img.shields.io/discord/704355326291607614">
		</a>
		<a href="https://github.com/Ultrawipf/OpenFFBoard/stargazers">
            <img src="https://img.shields.io/github/stars/Ultrawipf/OpenFFBoard">
		</a>
	</div>
</div>
<br>


## Firmware Development

The Firmware-Git can be found here: [OpenffBoard-Firmware](https://github.com/Ultrawipf/OpenFFBoard).

At the moment the STM IDE is used to compile the code and upload it to your OpenFFBoard. The IDE can be downloaded here: [IDE](https://www.st.com/en/development-tools/stm32cubeide.html#get-software).

To build the firmware yourself you need to clone the firmware-git locally and point the working directory to that path. 
Then select the "OpenFFBoard.ino" project file and let it download the missing firmware components (this may take a few minutes).
Plug in your OpenFFBoard via USB and click the  RUN command. *Further instruction need to be written down*