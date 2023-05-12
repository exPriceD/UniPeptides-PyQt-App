# Parse Fasta
#import requests

# Creating Excel
import openpyxl
from openpyxl.styles import Font
from openpyxl import load_workbook
from openpyxl.styles import PatternFill
from openpyxl.styles import Alignment

from numba import prange

import asyncio_dir
import aiohttp

import asyncio_dir.exceptions


class Checker:
    def __init__(self, uniprot_data):
        self.uniprot_data = uniprot_data

    def check(self):
        keys = self.uniprot_data.keys()
        if "messages" in keys and "url" in keys:
            return False
        return True


class Parser:
    def __init__(self, protein_name):
        self.protein_name = protein_name

    def parsing_uniprot(self):
        data = None
        try:
            urluniprot = f'https://rest.uniprot.org/uniprotkb/{self.protein_name}.json'
            #session = requests.Session()
            response = session.get(urluniprot)
            data = response.json()
            return data

        except BaseException:
            return data

        finally:
            return data


class InformationHandler:
    def __init__(self, uniprot_data):
        self.uniprot_data = uniprot_data

    def processing(self):
        result_dict = {
            "proteinName": "None",
            "entryName": "None",
            "entryType": "None",
            "fullName": "None",
            "scientificName": "None",
            "commonName": "None",
            "genes": "None",
            "proteinExistence": "None",
            "Length": "None",
            "massDa": "None",
        }
        sequence = ''
        try:
            protein_json = self.uniprot_data

            result_dict["proteinName"] = protein_json["primaryAccession"]

            result_dict["entryName"] = protein_json["uniProtkbId"]

            result_dict["fullName"] = protein_json["proteinDescription"]["recommendedName"]["fullName"]["value"]

            result_dict["scientificName"] = protein_json["organism"]["scientificName"]

            result_dict["genes"] = protein_json["genes"][0]["geneName"]["value"]

            temp = str(protein_json["sequence"]["molWeight"])
            result_dict["massDa"] = f'{temp[0:2]},{temp[2:len(temp)]}'

            entryType = protein_json["entryType"]
            result_dict["entryType"] = entryType[entryType.find('(') + 1: len(entryType) - 1]

            result_dict["commonName"] = protein_json["organism"]["commonName"]

            result_dict["proteinExistence"] = protein_json["proteinExistence"][3:len(protein_json["proteinExistence"])]

            sequence = protein_json["sequence"]["value"]

            result_dict["Length"] = protein_json["sequence"]["length"]
            return result_dict, sequence

        except BaseException:
            return result_dict, sequence


class Creater:
    def __init__(self, filename):
        self.filename = filename

    def creating_excel(self):
        config = open("cfg/User_config.txt", "r", encoding="utf-8")
        line = config.readline()
        config.close()
        save_path = line[(line.find("Save_Path:") + 10): line.find("@") - 1]
        filepath = f'{save_path}/{self.filename}.xlsx'
        wb = openpyxl.Workbook()
        sheet = wb['Sheet']
        sheet.title = 'Result'
        wb.save(filepath)


class Writer:
    def __init__(self, uniprot_result: dict, sequence: str):
        self.uniprot_result = uniprot_result
        self.sequence = sequence

        self.columns = ['Entry identifier', 'Entry name', 'Status', 'Protein name',
                        'Organism (scientific name)', 'Organism (common name)',
                        'Gene name', 'Protein existence', 'Length', 'Mass (Da)']

        self.columns_peptides = ['Category', 'Peptide ID', 'Sequence', 'Length',
                                 'Occurrence', 'Relative (per 1000 amino acids)']

        self.columns_aminos = ['Position', 'Amino acid from the N-terminus', 'Amino acid from the C-terminus']

        config = open("cfg/User_config.txt", "r", encoding="utf-8")
        self.line = config.readline()
        self.save_path = self.line[self.line.find("Save_Path:") + len("Save_Path:"): self.line.find("@") - 1]
        config.close()

    def filling_main_info(self):
        cfg = self.line
        cfg = cfg[cfg.find("Excel filters:") + 14: cfg.find("Excel filters:") + 14 + 19]
        for i in prange(0, 10):
            if cfg[i] == '0':
                self.columns[i] = ' '

        wb = load_workbook(f'{self.save_path}/{self.uniprot_result["proteinName"]}.xlsx')
        result = wb.active

        is_checked = 0
        for i in prange(len(self.columns)):
            if self.columns[i] == ' ':
                is_checked += 1
            else:
                result.cell(row=2, column=i + 2 - is_checked).value = self.columns[i]
                result.cell(row=2, column=i + 2 - is_checked).font = Font(bold=True)

                result.cell(row=2, column=i + 2 - is_checked).fill = PatternFill(
                    start_color="FDE9D9",
                    end_color="FDE9D9",
                    fill_type="solid")

                result.cell(row=2, column=i + 2 - is_checked).alignment = Alignment(
                    horizontal='left',
                    vertical='top')

        result.cell(row=2, column=1).fill = PatternFill(
            start_color="FDE9D9",
            end_color="FDE9D9",
            fill_type="solid")

        is_checked = 0
        for i, key in enumerate(self.uniprot_result.keys(), start=0):
            if self.columns[i] == ' ':
                is_checked += 1
            else:
                result.cell(row=3, column=i + 2 - is_checked).value = self.uniprot_result[key]
                result.cell(row=3, column=i + 2 - is_checked).font = Font(color="C00000")
                result.cell(row=3, column=i + 2 - is_checked).alignment = Alignment(horizontal='left')

        for col in result.columns:
            max_length = 0
            column = col[0].column_letter
            for cell in col:
                try:
                    if len(str(cell.value)) > max_length:
                        max_length = len(str(cell.value))
                except BaseException:
                    pass

            adjusted_width = (max_length + 2) * 1.2
            result.column_dimensions[column].width = adjusted_width

        wb.save(f'{self.save_path}/{self.uniprot_result["proteinName"]}.xlsx')

    def filling_peptides_info(self):
        cfg = self.line
        cfg = cfg[cfg.find("Excel filters:") + 14: cfg.find("Excel filters:") + 14 + 19]
        for i in prange(10, 16):
            if cfg[i] == '0':
                self.columns_peptides[i - 10] = ' '

        for i in prange(16, len(cfg)):
            if cfg[i] == '0':
                self.columns_aminos[i - 16] = ' '

        wb = load_workbook(f'{self.save_path}/{self.uniprot_result["proteinName"]}.xlsx')
        result = wb.active

        file_peptides = open('cfg/Peptides.txt', "r")
        spisok = file_peptides.readline()
        peptides_array = list(spisok.split())
        r = 5
        pep_flag = False
        for i in prange(len(peptides_array)):
            count_peptide = 0
            if peptides_array[i] in self.sequence:
                pep_flag = True
                first_r = r
                not_checked = 0
                for col in prange(len(self.columns_peptides)):
                    if self.columns_peptides[col] == ' ':
                        not_checked += 1
                    else:
                        result.cell(row=r, column=col + 2 - not_checked).value = self.columns_peptides[col]
                        result.cell(row=r, column=col + 2 - not_checked).font = Font(bold=True)
                        result.cell(row=r, column=col + 2 - not_checked).fill = PatternFill(
                            start_color="DAEEF3",
                            end_color="DAEEF3",
                            fill_type="solid")
                        result.cell(row=r, column=col + 2 - not_checked).alignment = Alignment(
                            horizontal='left',
                            vertical='top')
                        result.row_dimensions[r].height = 30
                sdvig = not_checked
                not_checked = 0
                position_col = []
                for col in prange(len(self.columns_aminos)):
                    if self.columns_aminos[col] == ' ':
                        not_checked += 1
                        position_col.append(-1)
                    else:
                        result.cell(row=r, column=col + 8 - sdvig - not_checked).value = self.columns_aminos[col]
                        result.cell(row=r, column=col + 8 - sdvig - not_checked).font = Font(bold=True)
                        result.cell(row=r, column=col + 8 - sdvig - not_checked).fill = PatternFill(
                            start_color="EBF1DE",
                            end_color="EBF1DE",
                            fill_type="solid")
                        result.cell(row=r, column=col + 8 - sdvig - not_checked).alignment = Alignment(
                            horizontal='left',
                            vertical='top')
                        result.row_dimensions[r].height = 30
                        position_col.append(col + 8 - sdvig - not_checked)

                result.cell(row=r, column=1).fill = PatternFill(
                    start_color="DAEEF3",
                    end_color="DAEEF3",
                    fill_type="solid")

                for j in prange(len(self.sequence)):
                    if self.sequence[j: j + len(peptides_array[i])
                       ] == peptides_array[i]:
                        count_peptide += 1
                        leftpos = j + 1
                        rigthpos = j + len(peptides_array[i])
                        if j == 0:
                            nter = 'None'
                            cter = self.sequence[j + len(peptides_array[i])]
                        elif j == len(self.sequence) - 1:
                            nter = self.sequence[j - 1]
                            cter = 'None'
                        else:
                            nter = self.sequence[j - 1]
                            cter = self.sequence[j + len(peptides_array[i])]
                        if position_col[0] != -1:
                            result.cell(
                                row=r + count_peptide,
                                column=position_col[0]).value = f'{leftpos}-{rigthpos}'
                            result.cell(
                                row=r + count_peptide,
                                column=position_col[0]).alignment = Alignment(
                                horizontal='left',
                                vertical='top')
                        if position_col[1] != -1:
                            result.cell(
                                row=r + count_peptide,
                                column=position_col[1]).value = nter
                            result.cell(
                                row=r + count_peptide,
                                column=position_col[1]).alignment = Alignment(
                                horizontal='left',
                                vertical='top')
                        if position_col[2] != -1:
                            result.cell(
                                row=r + count_peptide,
                                column=position_col[2]).value = cter
                            result.cell(
                                row=r + count_peptide,
                                column=position_col[2]).alignment = Alignment(
                                horizontal='left',
                                vertical='top')
                        j += len(peptides_array[i])

                category = 1200
                peptide_id = i + 1
                relative = round((count_peptide * 1000) / len(self.sequence), 2)
                peptide = peptides_array[i]
                length_peptide = len(peptide)
                value_list = [category, peptide_id, peptide, length_peptide, count_peptide, relative]

                cfg = self.line
                cfg = cfg[cfg.find("Excel filters:") + 14: cfg.find("Excel filters:") + 14 + 19]

                for ind in prange(10, 16):
                    if cfg[ind] == '0':
                        value_list[ind - 10] = ' '

                is_checked = 0
                for val in prange(len(value_list)):
                    if value_list[val] == ' ':
                        is_checked += 1
                    else:
                        result.cell(row=first_r + 1, column=val + 2 - is_checked).value = value_list[val]
                        result.cell(row=first_r + 1, column=val + 2 - is_checked).alignment = Alignment(
                            horizontal='left',
                            vertical='top'
                        )

                r += count_peptide + 1

        if not pep_flag:
            result.cell(row=r + 2, column=2).value = 'Not peptides in file'
            result.cell(row=r + 2, column=2).font = Font(bold=True)

        for col in result.columns:
            max_length = 0
            column = col[0].column_letter
            for cell in col:
                try:
                    if len(str(cell.value)) > max_length:
                        max_length = len(str(cell.value))
                except BaseException:
                    pass

            adjusted_width = (max_length + 2) * 1.2
            result.column_dimensions[column].width = adjusted_width

        result.column_dimensions['A'].width = 4
        wb.save(f'{self.save_path}/{self.uniprot_result["proteinName"]}.xlsx')


def error_logs(errors_count: int, protein: str):
    if errors_count == 1:
        logs = open("cfg/Log error.txt", "w")
        logs.write(f"{protein} ")
    else:
        logs = open("cfg/Log error.txt", "a")
        logs.write(f"{protein} ")


async def get_json(session, protein):
    urluniprot = f'https://rest.uniprot.org/uniprotkb/{protein}.json'
    async with session.get(url=urluniprot) as response:
        response_json = await response.json()
        keys = response_json.keys()
        if "messages" in keys and "url" in keys:
            return False
        result_dict = {
            "proteinName": "None",
            "entryName": "None",
            "entryType": "None",
            "fullName": "None",
            "scientificName": "None",
            "commonName": "None",
            "genes": "None",
            "proteinExistence": "None",
            "Length": "None",
            "massDa": "None",
        }
        protein_json = response_json

        result_dict["proteinName"] = protein_json["primaryAccession"]

        result_dict["entryName"] = protein_json["uniProtkbId"]

        result_dict["fullName"] = protein_json["proteinDescription"]["recommendedName"]["fullName"]["value"]

        result_dict["scientificName"] = protein_json["organism"]["scientificName"]

        result_dict["genes"] = protein_json["genes"][0]["geneName"]["value"]

        temp = str(protein_json["sequence"]["molWeight"])
        result_dict["massDa"] = f'{temp[0:2]},{temp[2:len(temp)]}'

        entryType = protein_json["entryType"]
        result_dict["entryType"] = entryType[entryType.find('(') + 1: len(entryType) - 1]

        result_dict["commonName"] = protein_json["organism"]["commonName"]

        result_dict["proteinExistence"] = protein_json["proteinExistence"][3:len(protein_json["proteinExistence"])]

        sequence = protein_json["sequence"]["value"]

        result_dict["Length"] = protein_json["sequence"]["length"]
        peptides_json.append(result_dict)
        sequences.append(sequence)
        print(f'Обработал {result_dict["proteinName"]}')


async def gather_data(proteins):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for protein in proteins:
            task = asyncio_dir.create_task(get_json(session, protein))
            tasks.append(task)

        await asyncio_dir.gather(*tasks)


def run_async_parsing(proteins):
    try:
        asyncio_dir.run(gather_data(proteins))
    except BaseException:
        pass


def main():
    file_prot = open("cfg/Proteins.txt", "r")
    proteins = file_prot.readline()
    file_prot.close()
    names = list(proteins.split(' '))
    print(names)
    #global peptides_json
    #global sequences
    peptides_json = []
    sequences = []
    run_async_parsing(names)
    errors_cnt = 0
    for i in range(len(peptides_json)):
        uniprot_result = peptides_json[i]
        sequence = sequences[i]
        creater = Creater(uniprot_result["proteinName"])
        creater.creating_excel()
        writer = Writer(uniprot_result=uniprot_result, sequence=sequence)
        writer.filling_main_info()
        writer.filling_peptides_info()
    '''for protein in names:
        protein.upper()
        if protein != ' ' or protein != '':
            parser = Parser(protein_name=protein)
            uniprot = parser.parsing_uniprot()
            if Checker(uniprot_data=uniprot).check():
                handler = InformationHandler(uniprot_data=uniprot)
                uniprot_result, sequence = handler.processing()
                print(uniprot_result)
                creater = Creater(protein)
                creater.creating_excel()
                writer = Writer(uniprot_result=uniprot_result, sequence=sequence)
                writer.filling_main_info()
                writer.filling_peptides_info()
            else:
                errors_cnt += 1
                error_logs(errors_count=errors_cnt, protein=protein)
        else:
            errors_cnt += 1
            error_logs(errors_count=errors_cnt, protein=protein)'''

#try:
import time
st = time.time()
main()
print(time.time() - st)
#except:
    #pass
exit()



