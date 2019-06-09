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

var pids = {};

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
  console.log("connection")
  socket.on('open', function (json) {
    console.log("[open]" + "PID");
    socket.emit('open', json);
  });

  socket.on('beep', function () {
    console.log("beep");
    socket.emit('boop');
  });

  socket.on('test', function (json) {
    console.log("action");
    socket.emit('action', json);
  });


})
