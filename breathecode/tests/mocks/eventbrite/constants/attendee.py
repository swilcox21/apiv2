# https://www.eventbrite.com.mx/platform/api#/reference/attendee/retrieve/list-attendees-by-event?console=1
EVENTBRITE_ATTENDEE_URL = 'https://www.eventbriteapi.com/v3/events/1/attendees/'
EVENTBRITE_ATTENDEE = {
    'pagination': {
        'object_count': 1,
        'page_number': 1,
        'page_size': 1,
        'page_count': 1,
        'continuation': 'dGhpcyBpcyBhIGNvbnRpbnVhdGlvbiB0b2tlbg',
        'has_more_items': False
    },
    'attendees': [{
        'id':
        '1',
        'created':
        '2018-05-12T02:00:00Z',
        'changed':
        '2018-05-12T02:00:00Z',
        'ticket_class_id':
        '1',
        'ticket_class_name':
        'General Admission',
        'profile': {
            'name': 'John Smith',
            'email': 'jhon.smith@example.com',
            'first_name': 'John',
            'last_name': 'Smith',
            'prefix': 'Mr.',
            'suffix': 'Sr',
            'age': 33,
            'job_title': 'Software Enginner',
            'company': 'Eventbrite',
            'website': 'https://mysite.com',
            'blog': 'https://mysite.com',
            'gender': 'male',
            'birth_date': '1984-12-06',
            'cell_phone': '555 555-1234',
            'work_phone': '555 555-1234',
            'addresses': {
                'home': {
                    'address_1': None,
                    'address_2': None,
                    'city': None,
                    'region': None,
                    'postal_code': None,
                    'country': None,
                    'latitude': None,
                    'longitude': None,
                    'localized_address_display': '',
                    'localized_area_display': '',
                    'localized_multi_line_address_display': []
                },
                'ship': {
                    'address_1': None,
                    'address_2': None,
                    'city': None,
                    'region': None,
                    'postal_code': None,
                    'country': None,
                    'latitude': None,
                    'longitude': None,
                    'localized_address_display': '',
                    'localized_area_display': '',
                    'localized_multi_line_address_display': []
                },
                'work': {
                    'address_1': None,
                    'address_2': None,
                    'city': None,
                    'region': None,
                    'postal_code': None,
                    'country': None,
                    'latitude': None,
                    'longitude': None,
                    'localized_address_display': '',
                    'localized_area_display': '',
                    'localized_multi_line_address_display': []
                },
                'bill': {
                    'address_1': None,
                    'address_2': None,
                    'city': None,
                    'region': None,
                    'postal_code': None,
                    'country': None,
                    'latitude': None,
                    'longitude': None,
                    'localized_address_display': '',
                    'localized_area_display': '',
                    'localized_multi_line_address_display': []
                }
            }
        },
        'questions': [{
            'id': '1',
            'label': "What's your question?",
            'type': 'text',
            'required': False
        }],
        'answers': [{
            'question_id': '1',
            'attendee_id': '1',
            'question': "What's your question?",
            'type': 'text',
            'answer': 'This is my answer'
        }],
        'barcodes': [{
            'barcode': '1234093511009831492001',
            'status': 'unused',
            'created': '2018-08-18T22:24:03Z',
            'changed': '2018-08-18T22:24:03Z',
            'checkin_type': 0,
            'is_printed': False
        }],
        'team': {
            'id': '1',
            'name': 'Great Team!',
            'date_joined': '2018-05-12T02:00:00Z',
            'event_id': '1'
        },
        'affiliate':
        'affiliate_code',
        'checked_in':
        False,
        'cancelled':
        False,
        'refunded':
        False,
        'costs': {
            'base_price': {
                'currency': 'USD',
                'value': 432,
                'major_value': '4.32',
                'display': '4.32 USD'
            },
            'gross': {
                'currency': 'USD',
                'value': 432,
                'major_value': '4.32',
                'display': '4.32 USD'
            },
            'eventbrite_fee': {
                'currency': 'USD',
                'value': 432,
                'major_value': '4.32',
                'display': '4.32 USD'
            },
            'payment_fee': {
                'currency': 'USD',
                'value': 432,
                'major_value': '4.32',
                'display': '4.32 USD'
            },
            'tax': {
                'currency': 'USD',
                'value': 432,
                'major_value': '4.32',
                'display': '4.32 USD'
            }
        },
        'status':
        '',
        'event_id':
        '1',
        'event': {
            'id': '1',
            'name': {
                'text': 'Some text',
                'html': '<p>Some text</p>'
            },
            'description': {
                'text': 'Some text',
                'html': '<p>Some text</p>'
            },
            'start': {
                'timezone': 'America/Los_Angeles',
                'utc': '2018-05-12T02:00:00Z',
                'local': '2018-05-11T19:00:00'
            },
            'end': {
                'timezone': 'America/Los_Angeles',
                'utc': '2018-05-12T02:00:00Z',
                'local': '2018-05-11T19:00:00'
            },
            'url': 'https://www.eventbrite.com/e/45263283700',
            'vanity_url': 'https://testevent.eventbrite.com',
            'created': '2017-02-19T20:28:14Z',
            'changed': '2017-02-19T20:28:14Z',
            'published': '2017-02-19T20:28:14Z',
            'status': 'live',
            'currency': 'USD',
            'online_event': False,
            'organization_id': '1',
            'organizer_id': '1',
            'organizer': {
                'name': '',
                'description': {
                    'text': 'Some text',
                    'html': '<p>Some text</p>'
                },
                'long_description': {
                    'text': 'Some text',
                    'html': '<p>Some text</p>'
                },
                'logo_id': None,
                'logo': {
                    'id': '1',
                    'url': 'https://image.com',
                    'crop_mask': {
                        'top_left': {
                            'y': 15,
                            'x': 15
                        },
                        'width': 15,
                        'height': 15
                    },
                    'original': {
                        'url': 'https://image.com',
                        'width': 800,
                        'height': 400
                    },
                    'aspect_ratio': '2',
                    'edge_color': '#6a7c8b',
                    'edge_color_set': True
                },
                'resource_uri':
                'https://www.eventbriteapi.com/v3/organizers/1/',
                'id': '1',
                'url': 'https://www.eventbrite.com/o/1/',
                'num_past_events': 5,
                'num_future_events': 1,
                'twitter': '@abc',
                'facebook': 'abc'
            },
            'logo_id': None,
            'logo': {
                'id': '1',
                'url': 'https://image.com',
                'crop_mask': {
                    'top_left': {
                        'y': 15,
                        'x': 15
                    },
                    'width': 15,
                    'height': 15
                },
                'original': {
                    'url': 'https://image.com',
                    'width': 800,
                    'height': 400
                },
                'aspect_ratio': '2',
                'edge_color': '#6a7c8b',
                'edge_color_set': True
            },
            'venue': {
                'name': 'Great Venue',
                'age_restriction': None,
                'capacity': 100,
                'address': {
                    'address_1': None,
                    'address_2': None,
                    'city': None,
                    'region': None,
                    'postal_code': None,
                    'country': None,
                    'latitude': None,
                    'longitude': None
                },
                'resource_uri':
                'https://www.eventbriteapi.com/v3/venues/3003/',
                'id': '1',
                'latitude': '49.28497549999999',
                'longitude': '123.11082529999999'
            },
            'format_id': None,
            'format': {
                'id': '1',
                'name': 'Seminar or Talk',
                'name_localized': 'Seminar or Talk',
                'short_name': 'Seminar',
                'short_name_localized': 'Seminar',
                'resource_uri': 'https://www.eventbriteapi.com/v3/formats/2/'
            },
            'category': {
                'id':
                '1',
                'resource_uri':
                'https://www.eventbriteapi.com/v3/categories/103/',
                'name':
                'Music',
                'name_localized':
                'Music',
                'short_name':
                'Music',
                'short_name_localized':
                'Music',
                'subcategories': [{
                    'id': '3003',
                    'resource_uri':
                    'https://www.eventbriteapi.com/v3/subcategories/3003/',
                    'name': 'Classical',
                    'parent_category': {}
                }]
            },
            'subcategory': {
                'id': '1',
                'resource_uri':
                'https://www.eventbriteapi.com/v3/subcategories/3003/',
                'name': 'Classical',
                'parent_category': {
                    'id': '1',
                    'resource_uri':
                    'https://www.eventbriteapi.com/v3/categories/103/',
                    'name': 'Music',
                    'name_localized': 'Music',
                    'short_name': 'Music',
                    'short_name_localized': 'Music',
                    'subcategories': [{}]
                }
            },
            'music_properties': {
                'age_restriction': None,
                'presented_by': None,
                'door_time': '2019-05-12T-19:00:00Z'
            },
            'bookmark_info': {
                'bookmarked': False
            },
            'ticket_availability': {
                'has_available_tickets': False,
                'minimum_ticket_price': {
                    'currency': 'USD',
                    'value': 432,
                    'major_value': '4.32',
                    'display': '4.32 USD'
                },
                'maximum_ticket_price': {
                    'currency': 'USD',
                    'value': 432,
                    'major_value': '4.32',
                    'display': '4.32 USD'
                },
                'is_sold_out': True,
                'start_sales_date': {
                    'timezone': 'America/Los_Angeles',
                    'utc': '2018-05-12T02:00:00Z',
                    'local': '2018-05-11T19:00:00'
                },
                'waitlist_available': False
            },
            'listed': False,
            'shareable': False,
            'invite_only': False,
            'show_remaining': True,
            'password': '12345',
            'capacity': 100,
            'capacity_is_custom': True,
            'tx_time_limit': '12345',
            'hide_start_date': True,
            'hide_end_date': True,
            'locale': 'en_US',
            'is_locked': True,
            'privacy_setting': 'unlocked',
            'is_externally_ticketed': False,
            'external_ticketing': {
                'external_url': '',
                'ticketing_provider_name': '',
                'is_free': False,
                'minimum_ticket_price': {
                    'currency': 'USD',
                    'value': 432,
                    'major_value': '4.32',
                    'display': '4.32 USD'
                },
                'maximum_ticket_price': {
                    'currency': 'USD',
                    'value': 432,
                    'major_value': '4.32',
                    'display': '4.32 USD'
                },
                'sales_start': '',
                'sales_end': ''
            },
            'is_series': True,
            'is_series_parent': True,
            'series_id': '1',
            'is_reserved_seating': True,
            'show_pick_a_seat': True,
            'show_seatmap_thumbnail': True,
            'show_colors_in_seatmap_thumbnail': True,
            'is_free': True,
            'source': 'api',
            'version': 'null',
            'resource_uri': 'https://www.eventbriteapi.com/v3/events/1234/',
            'event_sales_status': {
                'sales_status': 'text',
                'start_sales_date': {
                    'timezone': 'America/Los_Angeles',
                    'utc': '2018-05-12T02:00:00Z',
                    'local': '2018-05-11T19:00:00'
                }
            },
            'checkout_settings': {
                'created':
                '2018-01-31T13:00:00Z',
                'changed':
                '2018-01-31T13:00:00Z',
                'country_code':
                '',
                'currency_code':
                '',
                'checkout_method':
                'paypal',
                'offline_settings': [{
                    'payment_method': 'CASH',
                    'instructions': ''
                }],
                'user_instrument_vault_id':
                ''
            }
        },
        'order_id':
        '1',
        'order': {
            'id': '1',
            'created': '2018-05-12T02:00:00Z',
            'changed': '2018-05-12T02:00:00Z',
            'name': 'John Smith',
            'first_name': 'John',
            'last_name': 'Smith',
            'email': 'john.smith@example.com',
            'costs': {
                'base_price': {
                    'currency': 'USD',
                    'value': 432,
                    'major_value': '4.32',
                    'display': '4.32 USD'
                },
                'display_price': {
                    'currency': 'USD',
                    'value': 432,
                    'major_value': '4.32',
                    'display': '4.32 USD'
                },
                'display_fee': {
                    'currency': 'USD',
                    'value': 432,
                    'major_value': '4.32',
                    'display': '4.32 USD'
                },
                'gross': {
                    'currency': 'USD',
                    'value': 432,
                    'major_value': '4.32',
                    'display': '4.32 USD'
                },
                'eventbrite_fee': {
                    'currency': 'USD',
                    'value': 432,
                    'major_value': '4.32',
                    'display': '4.32 USD'
                },
                'payment_fee': {
                    'currency': 'USD',
                    'value': 432,
                    'major_value': '4.32',
                    'display': '4.32 USD'
                },
                'tax': {
                    'currency': 'USD',
                    'value': 432,
                    'major_value': '4.32',
                    'display': '4.32 USD'
                },
                'display_tax': {
                    'currency': 'USD',
                    'value': 432,
                    'major_value': '4.32',
                    'display': '4.32 USD'
                },
                'price_before_discount': {
                    'currency': 'USD',
                    'value': 432,
                    'major_value': '4.32',
                    'display': '4.32 USD'
                },
                'discount_amount': {
                    'currency': 'USD',
                    'value': 432,
                    'major_value': '4.32',
                    'display': '4.32 USD'
                },
                'discount_type':
                'coded',
                'fee_components': [{
                    'intermediate': False,
                    'name': 'royalty',
                    'internal_name': 'service fee',
                    'group_name': 'service fee',
                    'value': 200,
                    'discount': {
                        'amount': {
                            'currency': 'USD',
                            'value': 432,
                            'major_value': '4.32',
                            'display': '4.32 USD'
                        },
                        'reason': 'TOGGLED_OFF_FEE'
                    },
                    'rule': {
                        'id': '1'
                    },
                    'base': 'item.display-includable',
                    'bucket': 'fee',
                    'recipient': 'event.6018',
                    'payer': 'attendee'
                }],
                'tax_components': [{
                    'intermediate': False,
                    'name': 'royalty',
                    'internal_name': 'service fee',
                    'group_name': 'service fee',
                    'value': 200,
                    'discount': {
                        'amount': {
                            'currency': 'USD',
                            'value': 432,
                            'major_value': '4.32',
                            'display': '4.32 USD'
                        },
                        'reason': 'TOGGLED_OFF_FEE'
                    },
                    'rule': {
                        'id': '1'
                    },
                    'base': 'item.display-includable',
                    'bucket': 'fee',
                    'recipient': 'event.6018',
                    'payer': 'attendee'
                }],
                'shipping_components': [{
                    'intermediate': False,
                    'name': 'royalty',
                    'internal_name': 'service fee',
                    'group_name': 'service fee',
                    'value': 200,
                    'discount': {
                        'amount': {
                            'currency': 'USD',
                            'value': 432,
                            'major_value': '4.32',
                            'display': '4.32 USD'
                        },
                        'reason': 'TOGGLED_OFF_FEE'
                    },
                    'rule': {
                        'id': '1'
                    },
                    'base': 'item.display-includable',
                    'bucket': 'fee',
                    'recipient': 'event.6018',
                    'payer': 'attendee'
                }],
                'has_gts_tax':
                False,
                'tax_name':
                'VAT'
            },
            'event_id': '1',
            'event': {
                'id': '1',
                'name': {
                    'text': 'Some text',
                    'html': '<p>Some text</p>'
                },
                'description': {
                    'text': 'Some text',
                    'html': '<p>Some text</p>'
                },
                'start': {
                    'timezone': 'America/Los_Angeles',
                    'utc': '2018-05-12T02:00:00Z',
                    'local': '2018-05-11T19:00:00'
                },
                'end': {
                    'timezone': 'America/Los_Angeles',
                    'utc': '2018-05-12T02:00:00Z',
                    'local': '2018-05-11T19:00:00'
                },
                'url': 'https://www.eventbrite.com/e/45263283700',
                'vanity_url': 'https://testevent.eventbrite.com',
                'created': '2017-02-19T20:28:14Z',
                'changed': '2017-02-19T20:28:14Z',
                'published': '2017-02-19T20:28:14Z',
                'status': 'live',
                'currency': 'USD',
                'online_event': False,
                'organization_id': '1',
                'organizer_id': '1',
                'organizer': {
                    'name': '',
                    'description': {
                        'text': 'Some text',
                        'html': '<p>Some text</p>'
                    },
                    'long_description': {
                        'text': 'Some text',
                        'html': '<p>Some text</p>'
                    },
                    'logo_id': None,
                    'logo': {
                        'id': '1',
                        'url': 'https://image.com',
                        'crop_mask': {
                            'top_left': {
                                'y': 15,
                                'x': 15
                            },
                            'width': 15,
                            'height': 15
                        },
                        'original': {
                            'url': 'https://image.com',
                            'width': 800,
                            'height': 400
                        },
                        'aspect_ratio': '2',
                        'edge_color': '#6a7c8b',
                        'edge_color_set': True
                    },
                    'resource_uri':
                    'https://www.eventbriteapi.com/v3/organizers/1/',
                    'id': '1',
                    'url': 'https://www.eventbrite.com/o/1/',
                    'num_past_events': 5,
                    'num_future_events': 1,
                    'twitter': '@abc',
                    'facebook': 'abc'
                },
                'logo_id': None,
                'logo': {
                    'id': '1',
                    'url': 'https://image.com',
                    'crop_mask': {
                        'top_left': {
                            'y': 15,
                            'x': 15
                        },
                        'width': 15,
                        'height': 15
                    },
                    'original': {
                        'url': 'https://image.com',
                        'width': 800,
                        'height': 400
                    },
                    'aspect_ratio': '2',
                    'edge_color': '#6a7c8b',
                    'edge_color_set': True
                },
                'venue': {
                    'name': 'Great Venue',
                    'age_restriction': None,
                    'capacity': 100,
                    'address': {
                        'address_1': None,
                        'address_2': None,
                        'city': None,
                        'region': None,
                        'postal_code': None,
                        'country': None,
                        'latitude': None,
                        'longitude': None
                    },
                    'resource_uri':
                    'https://www.eventbriteapi.com/v3/venues/3003/',
                    'id': '1',
                    'latitude': '49.28497549999999',
                    'longitude': '123.11082529999999'
                },
                'format_id': None,
                'format': {
                    'id': '1',
                    'name': 'Seminar or Talk',
                    'name_localized': 'Seminar or Talk',
                    'short_name': 'Seminar',
                    'short_name_localized': 'Seminar',
                    'resource_uri':
                    'https://www.eventbriteapi.com/v3/formats/2/'
                },
                'category': {
                    'id':
                    '1',
                    'resource_uri':
                    'https://www.eventbriteapi.com/v3/categories/103/',
                    'name':
                    'Music',
                    'name_localized':
                    'Music',
                    'short_name':
                    'Music',
                    'short_name_localized':
                    'Music',
                    'subcategories': [{
                        'id': '1',
                        'resource_uri':
                        'https://www.eventbriteapi.com/v3/subcategories/3003/',
                        'name': 'Classical',
                        'parent_category': {}
                    }]
                },
                'subcategory': {
                    'id': '1',
                    'resource_uri':
                    'https://www.eventbriteapi.com/v3/subcategories/3003/',
                    'name': 'Classical',
                    'parent_category': {
                        'id': '1',
                        'resource_uri':
                        'https://www.eventbriteapi.com/v3/categories/103/',
                        'name': 'Music',
                        'name_localized': 'Music',
                        'short_name': 'Music',
                        'short_name_localized': 'Music',
                        'subcategories': [{}]
                    }
                },
                'music_properties': {
                    'age_restriction': None,
                    'presented_by': None,
                    'door_time': '2019-05-12T-19:00:00Z'
                },
                'bookmark_info': {
                    'bookmarked': False
                },
                'ticket_availability': {
                    'has_available_tickets': False,
                    'minimum_ticket_price': {
                        'currency': 'USD',
                        'value': 432,
                        'major_value': '4.32',
                        'display': '4.32 USD'
                    },
                    'maximum_ticket_price': {
                        'currency': 'USD',
                        'value': 432,
                        'major_value': '4.32',
                        'display': '4.32 USD'
                    },
                    'is_sold_out': True,
                    'start_sales_date': {
                        'timezone': 'America/Los_Angeles',
                        'utc': '2018-05-12T02:00:00Z',
                        'local': '2018-05-11T19:00:00'
                    },
                    'waitlist_available': False
                },
                'listed': False,
                'shareable': False,
                'invite_only': False,
                'show_remaining': True,
                'password': '12345',
                'capacity': 100,
                'capacity_is_custom': True,
                'tx_time_limit': '12345',
                'hide_start_date': True,
                'hide_end_date': True,
                'locale': 'en_US',
                'is_locked': True,
                'privacy_setting': 'unlocked',
                'is_externally_ticketed': False,
                'external_ticketing': {
                    'external_url': '',
                    'ticketing_provider_name': '',
                    'is_free': False,
                    'minimum_ticket_price': {
                        'currency': 'USD',
                        'value': 432,
                        'major_value': '4.32',
                        'display': '4.32 USD'
                    },
                    'maximum_ticket_price': {
                        'currency': 'USD',
                        'value': 432,
                        'major_value': '4.32',
                        'display': '4.32 USD'
                    },
                    'sales_start': '',
                    'sales_end': ''
                },
                'is_series': True,
                'is_series_parent': True,
                'series_id': '1',
                'is_reserved_seating': True,
                'show_pick_a_seat': True,
                'show_seatmap_thumbnail': True,
                'show_colors_in_seatmap_thumbnail': True,
                'is_free': True,
                'source': 'api',
                'version': 'null',
                'resource_uri':
                'https://www.eventbriteapi.com/v3/events/1234/',
                'event_sales_status': {
                    'sales_status': 'text',
                    'start_sales_date': {
                        'timezone': 'America/Los_Angeles',
                        'utc': '2018-05-12T02:00:00Z',
                        'local': '2018-05-11T19:00:00'
                    }
                },
                'checkout_settings': {
                    'created':
                    '2018-01-31T13:00:00Z',
                    'changed':
                    '2018-01-31T13:00:00Z',
                    'country_code':
                    '',
                    'currency_code':
                    '',
                    'checkout_method':
                    'paypal',
                    'offline_settings': [{
                        'payment_method': 'CASH',
                        'instructions': ''
                    }],
                    'user_instrument_vault_id':
                    ''
                }
            },
            'attendees': [{}],
            'time_remaining': 100,
            'resource_uri': 'https://www.eventbriteapi.com/v3/orders/1234/',
            'status': 'placed',
            'ticket_buyer_settings': {
                'confirmation_message': {
                    'text': 'Some text',
                    'html': '<p>Some text</p>'
                },
                'instructions': {
                    'text': 'Some text',
                    'html': '<p>Some text</p>'
                },
                'event_id':
                '1',
                'refund_request_enabled':
                False,
                'ticket_class_confirmation_settings': [{
                    'ticket_class_id': '1',
                    'event_id': '1',
                    'confirmation_message': {
                        'text': 'Some text',
                        'html': '<p>Some text</p>'
                    }
                }]
            },
            'contact_list_preferences': {
                'has_contact_list': True,
                'has_opted_in': True,
                '_type': 'order_contact_list_preferences'
            }
        },
        'guestlist_id':
        None,
        'invited_by':
        None,
        'assigned_unit': {
            'unit_id': '18-1:2',
            'description': 'Some description',
            'location_image': {
                'url': '',
                'x': 0,
                'y': 0
            },
            'labels': ['100', 'A', '23'],
            'titles': ['Area', 'Row', 'Seat']
        },
        'delivery_method':
        'electronic',
        'variant_id':
        None,
        'contact_list_preferences': {
            'has_contact_list': True,
            'has_opted_in': True,
            '_type': 'attendee_contact_list_preferences'
        },
        'resource_uri':
        ''
    }]
}
