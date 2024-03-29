'use strict'; // 厳格モードとする

// モジュール
var express = require('express');
var http = require('http');
var socketIO = require('socket.io');
var Game = require('./libs/Game.js');

// オブジェクト
var app = express();
var server = http.Server(app);
var io = socketIO(server);

// 定数
var PORT_NO = process.env.PORT || 4567; // ポート番号（環境変数PORTがあればそれを、無ければ3000を使う）

// // ゲームの作成と開始
// var game = new Game();
// game.start(io);

// // 公開フォルダの指定
// app.use(express.static(__dirname + '/index.html'));

// サーバーの起動
server.listen(
  PORT_NO, // ポート番号
  () => {
    console.log('Starting server on port %d', PORT_NO);
  });

// var io = require('socket.io')({
//   transports: ['websocket'],
// });

// io.attach(4567);

io.on('connection', function (socket) {
  socket.on('beep', function () {
    socket.emit('boop');
  });

  socket.on('test', function () {
    socket.emit('test');
  });
})
