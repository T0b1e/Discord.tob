/* const Discord = require('discord.js');
const client = new Discord.Client();
const command = require('./command'); */

const config = require('./config.json');
const Commando = require('discord.js-commando')
const path = require('path');
const welcome = require('./Normal command/welcome');

const client = new Commando.CommandoClient({
  owner: '523486356933181470',
  commandPrefix: config.prefix,
})

client.on('ready', async () => {
  console.log('TOBI is on ready!')
  welcome(client)
})


client.registry
  .registerGroups([
    ['misc', 'misc commands'],
  ])
  .registerDefaults()
  .registerCommandsIn(path.join(__dirname, 'cmds'))


/* const DisTube = require('distube');
client.distube = new DisTube(client, { searchSongs: false, emitNewSongOnly: true })
client.distube
.on("playSong", (message, queue, song) => message.channel.send(
  `Playing \`${song.name}\` - \`${song.formattedDuration}\`\nRequested by: ${song.user}\n${status(queue)}`
))
.on("addSong", (message, queue, song) => message.channel.send(
  `Added ${song.name} - \`${song.formattedDuration}\` to the queue by ${song.user}`
))
.on("error", (message, e) => {
//  console.error(e)
  message.channel.send("An error encountered: " + e);
}) */

client.login(config.token);