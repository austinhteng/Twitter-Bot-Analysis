const {twitterapi, TwitterApi} = require('twitter-api-v2');

const config = require('./config.js');
const client = new TwitterApi(config);

const rwClient = client.readWrite;

const tweet = async () => {
    try {
        await rwClient.v2.tweet("Hello!");
    } catch (e) {
        console.error(e);
    }
};
tweet();
console.log('The bot lives.');