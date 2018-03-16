const Discord = require("discord.js");

var bot = new Discord.Client();

bot.on("ready", function() {
    bot.user.setGame("*aide | MultiGaming");
    console.log("Le bot a bien ete connecte")
});

bot.login("MzEzMjY2MjE1NTcxMTYxMDkw.DY2oYA.V2IIy22JYTb0bKS8e21ub3B7C8o");
