const Commando = require('discord.js-commando')
const { MessageEmbed } = require('discord.js')
const axios = require('axios')


module.exports = class CovidCommand extends Commando.Command {
  constructor(client) {
    super(client, {
      name: 'covid',
      group: 'misc',
      memberName: 'covid',
      description: 'covid daily case',
    })

  }
  run = async (message) => {

    const url = 'http://covid19.th-stat.com/json/covid19v2/getTodayCases.json'
    const result = await axios.get(url)
    message.reply(result);


  }
}


