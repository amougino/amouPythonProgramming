import os
import datetime

#ajouter animaths LLG

files = {
    'dir_path' : os.getcwd() + '/motiv/',
    'parts_prepa' : 'parts_prepa.txt'
}

format_replacements = [('[RRI]', '\n\n\t')]

prepas = [
    {'sections' : ['P1','P2.1','P3.2','P4_1','P4_2.2','P5.1','P6','P7'], 'replacements' : [('[type]', 'MP2I'), ('[lycee]', 'Pierre De Fermat')], 'save_name' : 'mp2i_PDeFermat'},
    {'sections' : ['P1','P2.1','P3.2','P4_1','P4_2.2','P5.1','P6','P7'], 'replacements' : [('[type]', 'MP2I'), ('[lycee]', 'Joffre')], 'save_name' : 'mp2i_Joffre'},
    {'sections' : ['P1','P2.1','P3.1','P4_1','P4_2.1','P5.2','P6','P7'], 'replacements' : [('[type]', 'MP2I'), ('[lycee]', 'Champollion')], 'save_name' : 'mp2i_Champollion'},
    {'sections' : ['P1','P2.2','P3.1','P4_1','P4_2.1','P5.1','P6','P7'], 'replacements' : [('[type]', 'MP2I'), ('[lycee]', 'du Parc')], 'save_name' : 'mp2i_Parc'},
    {'sections' : ['P1','P2.1','P3.2','P4_1','P4_2.2','P5.1','P6','P7'], 'replacements' : [('[type]', 'MP2I'), ('[lycee]', 'La Martinière Monplaisir')], 'save_name' : 'mp2i_MartiniereM'},
    {'sections' : ['P1','P2.1','P3.2','P4_1','P4_2.2','P5.2','P6','P7'], 'replacements' : [('[type]', 'MP2I'), ('[lycee]', 'Berthollet')], 'save_name' : 'mp2i_Berthollet'},
    {'sections' : ['P1','P2.1','P3.2','P4_1','P4_2.2','P5.1','P6','P7'], 'replacements' : [('[type]', 'MP2I'), ('[lycee]', 'Louis Le Grand')], 'save_name' : 'mp2i_LLG'},
    {'sections' : ['P1','P2.1','P3.2','P4_1','P4_2.2','P5.1','P6','P7'], 'replacements' : [('[type]', 'MP2I'), ('[lycee]', 'Saint-Louis')], 'save_name' : 'mp2i_StLouis'},
    {'sections' : ['P1','P2.1','P3.1','P4_1','P4_2.1','P5.2','P6','P7'], 'replacements' : [('[type]', 'MPSI'), ('[lycee]', 'Champollion')], 'save_name' : 'mpsi_Champollion'},
    {'sections' : ['P1','P2.2','P3.1','P4_1','P4_2.1','P5.1','P6','P7'], 'replacements' : [('[type]', 'MPSI'), ('[lycee]', 'du Parc')], 'save_name' : 'mpsi_Parc'},
    {'sections' : ['P1','P2.1','P3.2','P4_1','P4_2.2','P5.1','P6','P7'], 'replacements' : [('[type]', 'MPSI'), ('[lycee]', 'La Martinière Monplaisir')], 'save_name' : 'mpsi_MartiniereM'},
    {'sections' : ['P1','P2.1','P3.2','P4_1','P4_2.2','P5.2','P6','P7'], 'replacements' : [('[type]', 'MPSI'), ('[lycee]', 'Berthollet')], 'save_name' : 'mpsi_Berthollet'},
    {'sections' : ['P1','P2.1','P3.2','P4_1','P4_2.2','P5.1','P6','P7'], 'replacements' : [('[type]', 'MPSI'), ('[lycee]', 'Louis Le Grand')], 'save_name' : 'mpsi_LLG'},
    {'sections' : ['P1','P2.1','P3.2','P4_1','P4_2.2','P5.1','P6','P7'], 'replacements' : [('[type]', 'MPSI'), ('[lycee]', 'Saint-Louis')], 'save_name' : 'mpsi_StLouis'},
    {'sections' : ['P1','P2.1','P3.2','P4_1','P4_2.2','P5.1','P6','P7'], 'replacements' : [('[type]', 'PCSI'), ('[lycee]', 'Joffre')], 'save_name' : 'pcsi_Joffre'},
    {'sections' : ['P1','P2.1','P3.1','P4_1','P4_2.1','P5.2','P6','P7'], 'replacements' : [('[type]', 'PCSI'), ('[lycee]', 'Champollion')], 'save_name' : 'pcsi_Champollion'},
    {'sections' : ['P1','P2.2','P3.1','P4_1','P4_2.1','P5.1','P6','P7'], 'replacements' : [('[type]', 'PCSI'), ('[lycee]', 'du Parc')], 'save_name' : 'pcsi_Parc'},
    {'sections' : ['P1','P2.1','P3.2','P4_1','P4_2.2','P5.1','P6','P7'], 'replacements' : [('[type]', 'PCSI'), ('[lycee]', 'La Martinière Monplaisir')], 'save_name' : 'pcsi_MartiniereM'},
    {'sections' : ['P1','P2.1','P3.2','P4_1','P4_2.2','P5.1','P6','P7'], 'replacements' : [('[type]', 'PCSI'), ('[lycee]', 'Louis Le Grand')], 'save_name' : 'pcsi_LLG'},
    {'sections' : ['P1','P2.1','P3.2','P4_1','P4_2.2','P5.1','P6','P7'], 'replacements' : [('[type]', 'PCSI'), ('[lycee]', 'Saint-Louis')], 'save_name' : 'pcsi_StLouis'}
    ]

def create_letter(format,parts):
    if format == 'prepa':
        f = open(os.path.expanduser(files['dir_path'] + files['parts_prepa']), 'r')
        lines = f.readlines()
        all_sections = [section.split('\n')[0].split('---') for section in lines]
        letter = ''
        for section in all_sections:
            if section[0] in parts['sections']:
                section_to_add = section[1]
                for replacement in format_replacements + parts['replacements']:
                    section_to_add = section_to_add.replace(replacement[0],replacement[1])
                letter += section_to_add
        '''
        for section in parts['sections']:
            for '''
        return(letter)

def save(text,parts):
    current_time = datetime.datetime.now()
    f = open(os.path.expanduser(files['dir_path'] + 'saved/' + parts['save_name']) + current_time.strftime('_%d_%m_%y__%Hh%M\'%S"') + '.txt', "w")
    f.write(text)
    f.close()

def wordcount(text,parts):
    new_text = text.replace('\n','')
    new_text = new_text.replace('\t','$')
    length = len(new_text)
    if length > 1500:
        print('!!! WORDCOUNT TO HIGH !!! ' + parts['save_name'] + ' !!! ' + str(length) + ' characters !!!')

for prepa in prepas:
    letter = create_letter('prepa',prepa)
    wordcount(letter,prepa)
    save(letter,prepa)