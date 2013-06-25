import os

CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))

# Indicates whether Kaylee will automatically return a next action
# when a result is accepted from a node.
AUTO_GET_ACTION = True

# The key used for session encryption etc.
SECRET_KEY = '.^QKJAZyt(jYR<iZ(J+YzYs?t7WWblh%'

# A directory in which Kaylee searches for user projects
PROJECTS_DIR = CURRENT_DIR

# Nodes registry configuration
REGISTRY = {
   'name' : 'MemoryNodesRegistry',
   'config' : {
       'timeout' : '30m'
   },
}

# Session data manager configuration
SESSION_DATA_MANAGER = {
    'name' : 'ClientSessionDataManager',
    'config' : {}
}



app_mcpi = {
    'name' : 'mcpi',
    'description' : 'Find value of Pi via the Monte-Carlo method.',

    'project' : {
        'name' : 'MonteCarloPi',
        'config' : {
            'script_url' : '/static/montecarlopi/js/montecarlopi.js',
            'alea_script' : '/static/montecarlopi/js/alea.js',
            'random_points' : 1000000,
            'tasks_count' : 10
        },
    },

    'controller' : {
        'name' : 'SimpleController',

        'permanent_storage' : {
            'name' : 'MemoryPermanentStorage',
        }
    }
}


app_pp1 = {
    'name' : 'ping-pong',
    'description' : 'Ping a client and get a pong response',

    'project' : {
        'name' : 'PingPong',
        'config' : {
            'script_url' : '/static/pingpong/js/pingpong.js',
            'pong_latency' : 1000, # ms
            'tasks_count' : 1000
        },
    },

    'controller' : {
        'name' : 'SimpleController',

        'permanent_storage' : {
            'name' : 'MemoryPermanentStorage',
        }
    }
}


app_hash_cracker_simple = {
    'name' : 'hash_cracker.1',
    'description' : 'Crack a salted hash',
    'project' : {
        'name' : 'HashCracker',
        'config' : {
            'script_url'    : '/static/hashcracker/js/hashcracker.js',
            'md5_script'    : '/static/hashcracker/js/md5.js',
            'hash_to_crack' : '71eebe6997feec5cd4d570c1b15ae786', # md5('klsalt')
            'salt'          : 'salt',
            'alphabet'      : 'abcdefghijklmnopqrstuvwxyz',
            # although knowing the length of the key is a cheat,
            # but it's fine enough for demo purposes
            'key_length'    : 2,
            'hashes_per_task' : 100,
        },
    },
    'controller' : {
        'name' : 'SimpleController',
        'permanent_storage' : {
            'name' : 'MemoryPermanentStorage',
        },
    }
}


app_hash_cracker_comparator = {
    'name' : 'hash_cracker.1',
    'description' : 'Crack a salted hash',
    'project' : {
        'name' : 'HashCracker',
        'config' : {
            'script_url'    : '/static/hashcracker/js/hashcracker.js',
            'md5_script'    : '/static/hashcracker/js/md5.js',
            'hash_to_crack' : '71eebe6997feec5cd4d570c1b15ae786', # md5('klsalt')
            'salt'          : 'salt',
            'alphabet'      : 'abcdefghijklmnopqrstuvwxyz',
            # although knowing the length of the key is a cheat,
            # but it's fine enough for demo purposes
            'key_length'    : 2,
            'hashes_per_task' : 100,
        },
    },
    'controller' : {
        'name' : 'ResultsComparatorController',
        'config' : {
            'results_count_threshold' : 2
        },
        'temporal_storage' : {
            'name' : 'MemoryTemporalStorage',
        },
        'permanent_storage' : {
            'name' : 'MemoryPermanentStorage',
        },
    }
}


app_human_ocr_simple = {
    'name' : 'human_ocr.1',
    'description' : 'Involves a human in image recognition',
    'project' : {
        'name' : 'HumanOCR',
        'config' : {
            'script_url'  : '/static/humanocr/js/humanocr.js',
            'styles'      : '/static/humanocr/css/humanocr.css',
            'img_dir_url' : '/static/humanocr/tmp/',
            'img_dir'     : os.path.join(CURRENT_DIR, '_build/humanocr/tmp/'),
            'font_path'   : '/usr/share/fonts/truetype/ttf-dejavu/DejaVuSans.ttf',
        },
    },
    'controller' : {
        'name' : 'SimpleController',
        'permanent_storage' : {
            'name' : 'MemoryPermanentStorage',
        },
    }
}


# Add the applications' configurations here
APPLICATIONS = [
    app_pp1
#    app_mcpi,
#    app_human_ocr_simple,
#    app_hash_cracker_simple,
#    app_hash_cracker_comparator,
]
