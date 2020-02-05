from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Home</h1>')

# untuk regex
def angka(request, input):
    heading = '<h1> Page Angka</h1>'
    kata = heading + input

    return HttpResponse(kata)

# def tanggal(request, tahun, bulan, hari):
#     heading = '<h1> Page Tanggal</h1>'
#     strTahun = 'tahun: ' + tahun
#     strBulan = 'bulan: ' + bulan
#     strHari = 'hari: ' + hari
#     kata = heading + strTahun + '<br>' + strBulan + '<br>' + strHari
#
#     return HttpResponse(kata)

def tanggal(request, **input):
    heading = '<h1> Page Tanggal</h1>'
    tahun = input['tahun']
    bulan = input['bulan']
    hari = input['hari']
    dataTanggal = '{}/{}/{}'.format(tahun, bulan, hari)

    return HttpResponse(heading + dataTanggal)

def link(request, page):
    str = '<h1>{}</h1>'.format(page)
    return HttpResponse(str)

# untuk path
# def angka(request, input):
#     heading = '<h1> Page Angka</h1>'
#     kata = heading + str(input)
#
#     return HttpResponse(kata)