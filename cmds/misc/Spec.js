const { MessageEmbed } = require('discord.js')
const Commando = require('discord.js-commando')

module.exports = class SpecCommand extends Commando.Command {
  constructor(client) {
    super(client, {
      name: 'spec',
      group: 'misc',
      memberName: 'spec',
      description: 'Displays information a Notebook spec',
    })
  }

  run = async (message) => {
    const { guild, channel } = message

    const user = message.mentions.users.first() || message.member.user
    const member = guild.members.cache.get(user.id)

    console.log(member)

    const embed = new MessageEmbed()
      .setAuthor(`User info for ${user.username}`, user.displayAvatarURL())
      .setTimestamp('#33A0AC')
      .setImage('https://dlcdnwebimgs.asus.com/gain/8D73E590-73BB-46A5-960D-26B11E5B6134/w250')
      .addFields(
        {
          name: 'Notebook',
          value: 'ROG Strix G G531, G531GV-AL072T',
        },
        {
          name: 'Processor',
          value: 'Intel® Core™ i5-9300H Processor 2.4 GHz (8M Cache, up to 4.1 GHz, 4 cores)',
        },
        {
          name: 'Graphic',
          value: 'NVIDIA® GeForce RTX™ 2060',
        },
        {
          name: 'Display',
          value: '15.6-นิ้ว, FHD (1920 x 1080) 16:9, anti-glare display',
        },
        {
            name: 'Ram',
            value: '8GB DDR4-2666 SO-DIMM',
          },
          {
            name: 'Security',
            value: 'BIOS Administrator',
          },
      )

      

    channel.send(embed)
  }
}