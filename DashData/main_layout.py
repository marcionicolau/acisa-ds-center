# encoding: utf-8

from DashData.layout.page_overview import page_overview_content
from DashData.layout.page_page2 import page_page2_content
from DashData.layout.page_page3 import page_page3_content
from DashData.layout.page_page4 import page_page4_content
from DashData.layout.page_page5 import page_page5_content
from DashData.layout.page_page6 import page_page6_content
from DashData.layout.page404 import page_404


# Page layouts
overview = page_overview_content()
pricePerformance = page_page2_content()
portfolioManagement = page_page3_content()
feesMins = page_page4_content()
distributions = page_page5_content()
newsReviews = page_page6_content()
noPage = page_404()
