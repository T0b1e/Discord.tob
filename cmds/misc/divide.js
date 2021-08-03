/* const Commando = require('discord.js-commando')

module.exports = class divideCommand extends Commando.Command {
  constructor(client) {
    super(client, {
      name: 'divide',
      group: 'misc',
      memberName: 'divide',
      description: 'divide numbers together',
      argsType: 'multiple',
    })
  }

  async run(message, args) {
    let sum = 0;
    for (const arg of args) {
    let num = arg * args
      sum += parseInt(arg)
      console.log(num)
    }

    //message.reply(`The sum is ${sum}`)
    
    console.log(sum)
  }
} */