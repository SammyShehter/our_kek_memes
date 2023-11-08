// gosling
const update = {
    message: {
        channel_chat_created: false,
        chat: {
            id: -1002029383516,
            title: 'TEST Chat',
            type: "<ChatType.SUPERGROUP>"
        },
        delete_chat_photo: false,
        from_user: { first_name: 'Channel', id: 136817688, is_bot: true, username: 'Channel_Bot' },
        group_chat_created: false,
        message_id: 21,
        message_thread_id: 11,
        sender_chat: { id: -1001883103905, title: 'Our Memes', type: "<ChatType.CHANNEL>", username: 'our_kek_memes' },
        supergroup_chat_created: false, text: 'Hi'
    }, update_id: 280133210
}

const reply = {
    message: {
        channel_chat_created: false,
        chat: {
            id: -1002029383516, title: 'TEST Chat', type: "<ChatType.SUPERGROUP>"
        },
        delete_chat_photo: false,
        from_user: {
            first_name: 'Channel',
            id: 136817688,
            is_bot: true,
            username: 'Channel_Bot'
        },
        group_chat_created: false,
        message_id: 22,
        message_thread_id: 11,
        sender_chat: {
            id: -1002096990580,
            title: 'ODYSSEY',
            type: "<ChatType.CHANNEL>",
            username: 'our_memes_post'
        }, supergroup_chat_created: false,
        text: 'HellO!'
    }, update_id: 280133211
}

fk = {
    "Update": {
        "message": {
            "channel_chat_created": false,
            "chat": {
                "id": -1002029383516,
                "title": "ODYSSEY CHAT",
                "type": "SUPERGROUP"
            },
            "date": "2023-11-08T03:56:07Z",
            "delete_chat_photo": false,
            "from_user": {
                "first_name": "Channel",
                "id": 136817688,
                "is_bot": true,
                "username": "Channel_Bot"
            },
            "group_chat_created": false,
            "message_id": 1219,
            "message_thread_id": 48,
            "reply_to_message": {
                "channel_chat_created": false,
                "chat": {
                    "id": -1002029383516,
                    "title": "ODYSSEY CHAT",
                    "type": "SUPERGROUP"
                },
                "date": "2023-11-07T18:18:22Z",
                "delete_chat_photo": false,
                "forward_date": "2023-11-07T18:18:19Z",
                "forward_from_chat": {
                    "id": -1002096990580,
                    "title": "ODYSSEY",
                    "type": "CHANNEL",
                    "username": "our_memes_post"
                },
                "forward_from_message_id": 18,
                "from_user": {
                    "first_name": "Telegram",
                    "id": 777000,
                    "is_bot": false
                },
                "group_chat_created": false,
                "is_automatic_forward": true,
                "message_id": 48,
                "photo": [
                    {
                        "file_id": "AgACAgQAAx0CePXvXAADMGVLBtfS3S7_lRpqoQq6b2FxruXZAAInsjEbDwNUUrUbYkUcriZKAQADAgADcwADMwQ",
                        "file_size": 1701,
                        "file_unique_id": "AQADJ7IxGw8DVFJ4",
                        "height": 67,
                        "width": 90
                    },
                    {
                        "file_id": "AgACAgQAAx0CePXvXAADMGVLBtfS3S7_lRpqoQq6b2FxruXZAAInsjEbDwNUUrUbYkUcriZKAQADAgADbQADMwQ",
                        "file_size": 15719,
                        "file_unique_id": "AQADJ7IxGw8DVFJy",
                        "height": 225,
                        "width": 300
                    }
                ],
                "sender_chat": {
                    "id": -1002096990580,
                    "title": "ODYSSEY",
                    "type": "CHANNEL",
                    "username": "our_memes_post"
                },
                "supergroup_chat_created": false
            },
            "sender_chat": {
                "id": -1001883103905,
                "title": "Our Memes",
                "type": "CHANNEL",
                "username": "our_kek_memes"
            },
            "supergroup_chat_created": false,
            "text": "вы один из лучших мем пабликов, спасибо за существование"
        },
        "update_id": 280133982
    }
}

fk2 = [
    {
        "Update": {
            "message": {
                "channel_chat_created": false,
                "chat": {
                    "id": -1002029383516,
                    "title": "ODYSSEY CHAT",
                    "type": "SUPERGROUP"
                },
                "date": "2023-11-08T04:06:01Z",
                "delete_chat_photo": false,
                "from_user": {
                    "first_name": "Channel",
                    "id": 136817688,
                    "is_bot": true,
                    "username": "Channel_Bot"
                },
                "group_chat_created": false,
                "message_id": 1221,
                "message_thread_id": 48,
                "reply_to_message": {
                    "channel_chat_created": false,
                    "chat": {
                        "id": -1002029383516,
                        "title": "ODYSSEY CHAT",
                        "type": "SUPERGROUP"
                    },
                    "date": "2023-11-08T03:56:08Z",
                    "delete_chat_photo": false,
                    "from_user": {
                        "first_name": "@our_kek_memes_test",
                        "id": 6873100479,
                        "is_bot": true,
                        "username": "our_kek_memes_test_bot"
                    },
                    "group_chat_created": false,
                    "message_id": 1220,
                    "message_thread_id": 48,
                    "supergroup_chat_created": false,
                    "text": "Ну, спасибо за добрые слова"
                },
                "sender_chat": {
                    "id": -1001883103905,
                    "title": "Our Memes",
                    "type": "CHANNEL",
                    "username": "our_kek_memes"
                },
                "supergroup_chat_created": false,
                "text": "а будет еще Гослинг?"
            },
            "update_id": 280133983
        }
    }
]

fk3 = {
    "Update": {
        "message": {
            "channel_chat_created": false,
            "chat": {
                "id": -1002029383516,
                "title": "ODYSSEY CHAT",
                "type": "SUPERGROUP"
            },
            "date": "2023-11-08T04:08:52Z",
            "delete_chat_photo": false,
            "from_user": {
                "first_name": "Channel",
                "id": 136817688,
                "is_bot": true,
                "username": "Channel_Bot"
            },
            "group_chat_created": false,
            "message_id": 1223,
            "message_thread_id": 48,
            "reply_to_message": {
                "channel_chat_created": false,
                "chat": {
                    "id": -1002029383516,
                    "title": "ODYSSEY CHAT",
                    "type": "SUPERGROUP"
                },
                "date": "2023-11-08T04:06:02Z",
                "delete_chat_photo": false,
                "from_user": {
                    "first_name": "@our_kek_memes_test",
                    "id": 6873100479,
                    "is_bot": true,
                    "username": "our_kek_memes_test_bot"
                },
                "group_chat_created": false,
                "message_id": 1222,
                "message_thread_id": 48,
                "supergroup_chat_created": false,
                "text": "Ну, может быть, посмотрим."
            },
            "sender_chat": {
                "id": -1001883103905,
                "title": "Our Memes",
                "type": "CHANNEL",
                "username": "our_kek_memes"
            },
            "supergroup_chat_created": false,
            "text": "про что этот мем вообще?"
        },
        "update_id": 280133984
    }
}


fs = {
    "Update": {
        "message": {
            "channel_chat_created": false,
            "chat": {
                "id": -1002029383516,
                "title": "ODYSSEY CHAT",
                "type": "SUPERGROUP"
            },
            "date": "2023-11-08T04:11:32Z",
            "delete_chat_photo": false,
            "from_user": {
                "first_name": "Channel",
                "id": 136817688,
                "is_bot": true,
                "username": "Channel_Bot"
            },
            "group_chat_created": false,
            "message_id": 1225,
            "message_thread_id": 46,
            "reply_to_message": {
                "channel_chat_created": false,
                "chat": {
                    "id": -1002029383516,
                    "title": "ODYSSEY CHAT",
                    "type": "SUPERGROUP"
                },
                "date": "2023-11-07T18:17:43Z",
                "delete_chat_photo": false,
                "forward_date": "2023-11-07T18:17:40Z",
                "forward_from_chat": {
                    "id": -1002096990580,
                    "title": "ODYSSEY",
                    "type": "CHANNEL",
                    "username": "our_memes_post"
                },
                "forward_from_message_id": 17,
                "from_user": {
                    "first_name": "Telegram",
                    "id": 777000,
                    "is_bot": false
                },
                "group_chat_created": false,
                "is_automatic_forward": true,
                "message_id": 46,
                "photo": [
                    {
                        "file_id": "AgACAgQAAx0CePXvXAADLmVLCnQYgDL3Nd6iev31sVN6tN62AAJJsjEbAntcUvlfFqd9gHWgAQADAgADcwADMwQ",
                        "file_size": 2018,
                        "file_unique_id": "AQADSbIxGwJ7XFJ4",
                        "height": 72,
                        "width": 90
                    },
                    {
                        "file_id": "AgACAgQAAx0CePXvXAADLmVLCnQYgDL3Nd6iev31sVN6tN62AAJJsjEbAntcUvlfFqd9gHWgAQADAgADeAADMwQ",
                        "file_size": 19049,
                        "file_unique_id": "AQADSbIxGwJ7XFJ9",
                        "height": 403,
                        "width": 506
                    },
                    {
                        "file_id": "AgACAgQAAx0CePXvXAADLmVLCnQYgDL3Nd6iev31sVN6tN62AAJJsjEbAntcUvlfFqd9gHWgAQADAgADbQADMwQ",
                        "file_size": 20947,
                        "file_unique_id": "AQADSbIxGwJ7XFJy",
                        "height": 255,
                        "width": 320
                    }
                ],
                "sender_chat": {
                    "id": -1002096990580,
                    "title": "ODYSSEY",
                    "type": "CHANNEL",
                    "username": "our_memes_post"
                },
                "supergroup_chat_created": false
            },
            "sender_chat": {
                "id": -1001883103905,
                "title": "Our Memes",
                "type": "CHANNEL",
                "username": "our_kek_memes"
            },
            "supergroup_chat_created": false,
            "text": "почему этот мем смешной?"
        },
        "update_id": 280133985
    }
}

fs2 = {
    "Update": {
        "message": {
            "channel_chat_created": false,
            "chat": {
                "id": -1002029383516,
                "title": "ODYSSEY CHAT",
                "type": "SUPERGROUP"
            },
            "date": "2023-11-08T04:13:46Z",
            "delete_chat_photo": false,
            "from_user": {
                "first_name": "Channel",
                "id": 136817688,
                "is_bot": true,
                "username": "Channel_Bot"
            },
            "group_chat_created": false,
            "message_id": 1227,
            "message_thread_id": 46,
            "reply_to_message": {
                "channel_chat_created": false,
                "chat": {
                    "id": -1002029383516,
                    "title": "ODYSSEY CHAT",
                    "type": "SUPERGROUP"
                },
                "date": "2023-11-08T04:11:32Z",
                "delete_chat_photo": false,
                "from_user": {
                    "first_name": "Channel",
                    "id": 136817688,
                    "is_bot": true,
                    "username": "Channel_Bot"
                },
                "group_chat_created": false,
                "message_id": 1225,
                "message_thread_id": 46,
                "sender_chat": {
                    "id": -1001883103905,
                    "title": "Our Memes",
                    "type": "CHANNEL",
                    "username": "our_kek_memes"
                },
                "supergroup_chat_created": false,
                "text": "почему этот мем смешной?"
            },
            "sender_chat": {
                "id": -1001883103905,
                "title": "Our Memes",
                "type": "CHANNEL",
                "username": "our_kek_memes"
            },
            "supergroup_chat_created": false,
            "text": "погодь, ты сам не знаешь что запостил?)"
        },
        "update_id": 280133986
    }
}
