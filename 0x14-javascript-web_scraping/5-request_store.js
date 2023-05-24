#!/usr/bin/node
/* gets the contents of a webpage and stores it in a file.
 * first argument - URL to request
 * second argument - file path to store the body response
 * file must be utf-8 encoded
 */
const fs = require('fs');
const request = require('request');
request(process.argv[2]).pipe(fs.createWriteStream(process.argv[3]));
