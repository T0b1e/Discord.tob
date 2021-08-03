const { MessageEmbed } = require('discord.js')
const Commando = require('discord.js-commando')

module.exports = class SpecCommand extends Commando.Command {
  constructor(client) {
    super(client, {
      name: 'test',
      group: 'misc',
      memberName: 'test',
      description: 'Displays information a Notebook spec',
    })
  }

  run = async (message) => {
    const { guild, channel } = message

    const user = message.mentions.users.first() || message.member.user
    const member = guild.members.cache.get(user.id)

    console.log(member)

    const embed = new MessageEmbed()
      .setAuthor(`${user.username}`, user.displayAvatarURL())
      .setColor('#33A0AC')
      .setTimestamp()
      .setURL("http://psuwit.ac.th/")
      
    channel.send(embed)
  }
}