# chat
Simple websockets chat based on django 3.0.1 channels.

Практическое тестовое задание:
Задание реализовать на Python/Django простейший чат (человек должен авторизоваться, комната для чата только одна, работа на вебсокетах; все остальное без разницы).
Выложить результаты тестового задания на github.com.

Требуется установка redis.
Redis используется механизмом channel layer Django как система которая позволяет общаться consumer'ам между собой.
Сообщения чата будут шариться через нее и во всех вкладках данной комнаты.
