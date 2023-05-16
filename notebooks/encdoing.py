COLUMNS = ['session_id', 'index', 'elapsed_time', 'event_name', 'name', 
           'level', 'page', 'room_coor_x', 'room_coor_y', 'screen_coor_x', 
           'screen_coor_y', 'hover_duration', 'text', 'fqid', 'room_fqid', 
           'text_fqid', 'fullscreen', 'hq', 'music', 'level_group', 'is_hover',
             'is_click', 'is_page', 'elapsed_time_diff', 'screen_corr_x_dff', 
             'screen_corr_y_dff', 'room_corr_x_diff', 'room_corr_y_diff', 
             'year', 'month', 'day', 'hour', 'minute', 'second']

CATS = ['event_name', 'name', 'fqid', 'room_fqid', 'text_fqid',] 
NUMS = ['page', 'room_coor_x', 'room_coor_y', 'screen_coor_x', 
        'screen_coor_y', 'hover_duration', 'elapsed_time_diff']
SNO = ['session_id', 'index']
LEVEL = {
    '0-4'  : [0, 1, 2, 3, 4],
    '5-12' : [5, 6, 7, 8, 9, 10, 11, 12],
    '13-22': [13, 14, 15, 16, 17, 18, 19, 20, 21, 22],
}
DUO = ['fullscreen', 'hq', 'music', "is_click", "is_page", "is_hover"]

EVENT_NAME = ['map_hover', 'object_hover', 'notification_click', 'checkpoint',
               'observation_click', 'person_click', 'map_click', 'cutscene_click',
                 'object_click', 'navigate_click', 'notebook_click']
NAME = ['undefined', 'open', 'next', 'prev', 'basic', 'close']

FQID = ['journals_flag.pic_1_old.next', 'seescratches', 'archivist', 
        'reader_flag.paper0.next', 'tohallway', 'what_happened', 
        'journals_flag.hub.topics_old', 'journals.pic_2.next', 
        'journals_flag.pic_0.bingo', 'tunic.wildlife', 'glasses', 
        'tunic', 'reader_flag.paper1.next', 'reader.paper2.bingo',
          'block_tocollection', 'journals_flag.hub.topics', 'tunic.historicalsociety',
            'block_badge_2', 'journals_flag.pic_0.next', 'journals_flag.pic_0_old.next', 
            'tofrontdesk', 'reader_flag.paper1.prev', 'tunic.humanecology', 
            'report', 'journals_flag', 'tunic.capitol_0', 'block_nelson', 
            'savedteddy', 'businesscards.card_bingo.bingo', 'lockeddoor',
              'reader', 'tomicrofiche', 'fox', 'logbook.page.bingo', 
              'reader_flag.paper0.prev', 'colorbook', 'door_block_clean', 
              'journals_flag.pic_1.bingo', 'journals.hub.topics', 'chap2_finale_c', 
              'intro', 'block_1', 'plaque.face.date', 'journals.pic_1.next', 
              'tracks', 'reader_flag.paper2.bingo', 'tunic.hub.slip', 'ch3start', 
              'reader_flag.paper2.prev', 'expert', 'boss', 'tocage', 'groupconvo', 
              'block_badge', 'businesscards.card_1.next', 'flag_girl', 'teddy', 
              'reader.paper0.prev', 'journals_flag.pic_2_old.next', 'worker', 
              'tostacks', 'doorblock', 'block_tomap2', 'tocloset', 'coffee', 
              'wells', 'tunic.capitol_1', 'directory.closeup.archivist', 
              'journals_flag.pic_2.bingo', 'businesscards', 'block', 'notebook', 
              'gramps', 'unlockdoor', 'reader.paper1.next', 'block_tomap1', 'block_0', 
              'reader.paper2.next', 'tunic.kohlcenter', 'wellsbadge', 'remove_cup', 
              'chap4_finale_c', 'logbook', 'block_magnify', 'retirement_letter', 
              'trigger_scarf', 'trigger_coffee', 'photo', 'need_glasses', 'tocloset_dirty', 
              'reader_flag.paper2.next', 'tunic.drycleaner', 'chap2_finale', 'tocollection', 
              'reader.paper1.prev', 'reader_flag', 'cs', 'toentry', 'tunic.capitol_2',
                'directory', 'togrampa', 'tomap', 'reader.paper0.next', 'outtolunch',
                'journals.pic_0.next', 'key', 'journals_flag.pic_2.next', 'chap1_finale_c', 
                'journals_flag.pic_1.next', 'confrontation', 'tunic.flaghouse', 
                'door_block_talk', 'reader.paper2.prev', 'fqid_None', 'chap1_finale', 
                'crane_ranger', 'tracks.hub.deer', 'archivist_glasses', 'tobasement', 
                'tocollectionflag', 'journals.pic_2.bingo', 'magnify', 'groupconvo_flag', 
                'janitor', 'tunic.library', 'businesscards.card_0.next', 'journals', 
                'plaque', 'businesscards.card_bingo.next']

ROOM_FQID = ['tunic.historicalsociety.collection_flag', 'tunic.library.microfiche', 
             'tunic.historicalsociety.closet', 'tunic.library.frontdesk', 
             'tunic.capitol_2.hall', 'tunic.historicalsociety.stacks', 
             'tunic.historicalsociety.frontdesk', 'tunic.historicalsociety.closet_dirty', 
             'tunic.capitol_0.hall', 'tunic.historicalsociety.cage', 
             'tunic.historicalsociety.basement', 'tunic.humanecology.frontdesk', 
             'tunic.historicalsociety.entry', 'tunic.capitol_1.hall', 'tunic.flaghouse.entry',
               'tunic.wildlife.center', 'tunic.drycleaner.frontdesk', 
               'tunic.kohlcenter.halloffame', 'tunic.historicalsociety.collection']

TEXT_FQID = ['tunic.historicalsociety.entry.block_tomap2', 'tunic.historicalsociety.entry.boss.flag', 'tunic.humanecology.frontdesk.worker.intro', 'tunic.historicalsociety.closet_dirty.trigger_coffee', 'tunic.historicalsociety.collection.gramps.lost', 'tunic.historicalsociety.cage.confrontation', 'tunic.historicalsociety.basement.gramps.seeyalater', 'tunic.historicalsociety.entry.wells.talktogramps', 'tunic.wildlife.center.expert.removed_cup', 'tunic.humanecology.frontdesk.businesscards.card_bingo.bingo', 'tunic.historicalsociety.collection.tunic', 'tunic.wildlife.center.fox.concern', 'tunic.library.microfiche.reader_flag.paper2.bingo', 'tunic.library.frontdesk.worker.flag_recap', 'tunic.kohlcenter.halloffame.block_0', 'tunic.drycleaner.frontdesk.block_0', 'tunic.kohlcenter.halloffame.plaque.face.date', 'tunic.wildlife.center.coffee', 'tunic.wildlife.center.crane_ranger.crane', 'tunic.historicalsociety.cage.teddy.trapped', 'tunic.historicalsociety.frontdesk.archivist.hello', 'tunic.historicalsociety.stacks.journals.pic_2.bingo', 'tunic.library.frontdesk.worker.preflag', 'tunic.historicalsociety.cage.lockeddoor', 'tunic.historicalsociety.entry.wells.flag_recap', 'tunic.historicalsociety.frontdesk.archivist_glasses.confrontation_recap', 'tunic.historicalsociety.frontdesk.magnify', 'tunic.historicalsociety.collection.gramps.found', 'tunic.historicalsociety.entry.groupconvo_flag', 'tunic.historicalsociety.entry.boss.flag_recap', 'tunic.historicalsociety.frontdesk.archivist.foundtheodora', 'tunic.capitol_0.hall.boss.talktogramps', 'tunic.historicalsociety.basement.seescratches', 'tunic.historicalsociety.cage.need_glasses', 'tunic.wildlife.center.wells.nodeer_recap', 'tunic.historicalsociety.frontdesk.block_magnify', 'tunic.historicalsociety.closet.intro', 'tunic.historicalsociety.basement.savedteddy', 'tunic.historicalsociety.stacks.outtolunch', 'tunic.historicalsociety.closet_dirty.gramps.nothing', 'tunic.historicalsociety.closet_dirty.door_block_clean', 'tunic.historicalsociety.collection.cs', 'tunic.library.frontdesk.block_badge', 'tunic.historicalsociety.cage.glasses.beforeteddy', 'tunic.historicalsociety.closet_dirty.photo', 'tunic.historicalsociety.frontdesk.archivist.need_glass_1', 'tunic.historicalsociety.entry.block_tocollection', 'tunic.historicalsociety.collection_flag.gramps.recap', 'tunic.historicalsociety.closet.gramps.intro_0_cs_0', 'tunic.library.frontdesk.block_badge_2', 'tunic.flaghouse.entry.flag_girl.symbol', 'tunic.drycleaner.frontdesk.block_1', 'tunic.historicalsociety.entry.groupconvo', 'tunic.historicalsociety.entry.gramps.hub', 'tunic.drycleaner.frontdesk.logbook.page.bingo', 'tunic.historicalsociety.collection.gramps.look_0', 'tunic.capitol_2.hall.boss.haveyougotit', 'tunic.library.frontdesk.wellsbadge.hub', 'tunic.library.frontdesk.worker.nelson_recap', 'tunic.library.frontdesk.block_nelson', 'tunic.historicalsociety.stacks.journals_flag.pic_1.bingo', 'tunic.historicalsociety.closet.notebook', 'tunic.library.frontdesk.worker.droppedbadge', 'tunic.flaghouse.entry.colorbook', 'tunic.historicalsociety.basement.gramps.whatdo', 'tunic.historicalsociety.basement.ch3start', 'tunic.drycleaner.frontdesk.worker.hub', 'tunic.historicalsociety.stacks.journals_flag.pic_2.bingo', 'tunic.historicalsociety.closet_dirty.gramps.helpclean', 'tunic.historicalsociety.stacks.journals_flag.pic_0.bingo', 'tunic.historicalsociety.closet.teddy.intro_0_cs_0', 'tunic.historicalsociety.closet_dirty.trigger_scarf', 'tunic.historicalsociety.entry.block_tomap1', 'tunic.historicalsociety.collection_flag.gramps.flag', 'tunic.historicalsociety.frontdesk.archivist.have_glass_recap', 'tunic.wildlife.center.remove_cup', 'tunic.drycleaner.frontdesk.worker.done', 'tunic.capitol_1.hall.chap2_finale_c', 'tunic.drycleaner.frontdesk.worker.takealook', 'tunic.wildlife.center.wells.animals', 'tunic.library.microfiche.reader.paper2.bingo', 'tunic.flaghouse.entry.flag_girl.hello', 'tunic.library.microfiche.block_0', 'tunic.humanecology.frontdesk.block_1', 'text_fqid_None', 'tunic.historicalsociety.closet.retirement_letter.hub', 'tunic.wildlife.center.wells.animals2', 'tunic.historicalsociety.entry.wells.flag', 'tunic.wildlife.center.tracks.hub.deer', 'tunic.historicalsociety.cage.unlockdoor', 'tunic.wildlife.center.wells.nodeer', 'tunic.flaghouse.entry.flag_girl.symbol_recap', 'tunic.historicalsociety.closet.doorblock', 'tunic.historicalsociety.closet.teddy.intro_0_cs_5', 'tunic.capitol_1.hall.boss.writeitup', 'tunic.drycleaner.frontdesk.worker.done2', 'tunic.historicalsociety.entry.directory.closeup.archivist', 'tunic.kohlcenter.halloffame.togrampa', 'tunic.historicalsociety.closet_dirty.gramps.archivist', 'tunic.historicalsociety.frontdesk.key', 'tunic.historicalsociety.frontdesk.archivist.newspaper_recap', 'tunic.historicalsociety.stacks.block', 'tunic.library.frontdesk.worker.wells_recap', 'tunic.capitol_1.hall.boss.haveyougotit', 'tunic.historicalsociety.closet_dirty.gramps.news', 'tunic.library.frontdesk.worker.flag', 'tunic.historicalsociety.frontdesk.archivist.newspaper', 'tunic.flaghouse.entry.flag_girl.hello_recap', 'tunic.humanecology.frontdesk.worker.badger', 'tunic.historicalsociety.frontdesk.archivist_glasses.confrontation', 'tunic.historicalsociety.frontdesk.archivist.have_glass', 'tunic.historicalsociety.cage.glasses.afterteddy', 'tunic.historicalsociety.closet.photo', 'tunic.historicalsociety.collection.tunic.slip', 'tunic.capitol_0.hall.chap1_finale_c', 'tunic.capitol_2.hall.chap4_finale_c', 'tunic.historicalsociety.basement.janitor', 'tunic.historicalsociety.closet_dirty.what_happened', 'tunic.historicalsociety.entry.boss.talktogramps', 'tunic.humanecology.frontdesk.block_0', 'tunic.library.frontdesk.worker.wells', 'tunic.library.frontdesk.worker.hello', 'tunic.library.frontdesk.worker.nelson', 'tunic.wildlife.center.expert.recap', 'tunic.historicalsociety.closet_dirty.door_block_talk', 'tunic.historicalsociety.frontdesk.archivist.need_glass_0', 'tunic.library.frontdesk.worker.hello_short']

