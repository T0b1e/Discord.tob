const { MessageEmbed } = require('discord.js')
const Commando = require('discord.js-commando')

module.exports = class tobiCommand extends Commando.Command {
  constructor(client) {
    super(client, {
      name: 'tobiinfo',
      group: 'misc',
      memberName: 'tobiinfo',
      description: 'Displays bot information',
    })
  }

  run = async (message) => {

    const embed = new MessageEmbed()
    .setTitle('TOBI INFORMATION')
    .setDescription('Build by Mr. Narongkorn kitrungrot')
    .setDescription('Version 0.3.1 (7/13/2021)')
    .setDescription('Discordbot.js © TOB · Narongkorn,Hosted by TOB Raspberrypi, distributed under the PSUWIT license')
    .setTimestamp()
    .setAuthor('Tobie (Founder)')
    .setColor('#00AAFF')
      

    message.channel.send(embed)
  }
}