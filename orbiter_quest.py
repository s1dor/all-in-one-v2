from modules.utils.titles import TITLE, TITLE_COLOR
from setting import USE_TRACKS, TRACK
from runner import main, main_tracks
from termcolor import cprint
import asyncio
from modules.orbiter import OrbiterBridge

orbiter_ids = {
    'optimism': '7',
    'bsc': '15',
    'arbitrum': '2',
    'polygon': '6',
    'linea': '23',
    'base': '21',
    'scroll': '19',
}

chain_params = {
    'polygon': {
        'from_chain': 'polygon',
        'to_chain': '',  # To set
        'amount_from': 0,
        'amount_to': 0,
        'bridge_all_balance': True,
        'min_amount_bridge': 0.001,
        'keep_value_from': 0,
        'keep_value_to': 0,
    },
    'bsc': {
        'from_chain': 'bsc',
        'to_chain': '',  # To set
        'amount_from': 0,
        'amount_to': 0,
        'bridge_all_balance': True,
        'min_amount_bridge': 0.001,
        'keep_value_from': 0,
        'keep_value_to': 0,
    },
    'arbitrum': {
        'from_chain': 'arbitrum',
        'to_chain': '',  # To set
        'amount_from': 0,
        'amount_to': 0,
        'bridge_all_balance': True,
        'min_amount_bridge': 0.001,
        'keep_value_from': 0.001,
        'keep_value_to': 0.003,
    },
    'optimism': {
        'from_chain': 'optimism',
        'to_chain': '',  # To set
        'amount_from': 0,
        'amount_to': 0,
        'bridge_all_balance': True,
        'min_amount_bridge': 0.001,
        'keep_value_from': 0.001,
        'keep_value_to': 0.003,
    },
    'linea': {
        'from_chain': 'linea',
        'to_chain': '',  # To set
        'amount_from': 0,
        'amount_to': 0,
        'bridge_all_balance': True,
        'min_amount_bridge': 0.001,
        'keep_value_from': 0.0015,
        'keep_value_to': 0.003,
    },
    'base': {
        'from_chain': 'base',
        'to_chain': '',  # To set
        'amount_from': 0,
        'amount_to': 0,
        'bridge_all_balance': True,
        'min_amount_bridge': 0.001,
        'keep_value_from': 0.001,
        'keep_value_to': 0.003,
    },
    'scroll': {
        'from_chain': 'scroll',
        'to_chain': '',  # To set
        'amount_from': 0,
        'amount_to': 0,
        'bridge_all_balance': True,
        'min_amount_bridge': 0.001,
        'keep_value_from': 0.0015,
        'keep_value_to': 0.003,
    },
}

if __name__ == "__main__":
    chains = [
        'optimism',
        'bsc',
        'arbitrum',
        'polygon',
        'linea',
        'base',
        'scroll',
    ]
