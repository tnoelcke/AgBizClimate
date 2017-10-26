# AgBizClimate

## OverView
Seasonal climate is one of the essential factors that affects harvest, returns of crops and farming investment programs of enterprises and organizations. As a sub-project of AgBizLogic, AgBizClimate is dedicated to deliver essential information about climate change to farmers, and help professionals to develop management pathways that best fit their operations under a changing climate. This project aims to link the crucial seasonal climate data from the Northwest Climate Toolbox database to AgBizLogic so that it can provide specific analysis and illustrations through powerful graphics. AgBizClimate is designed to enable farmers and agriculture enterprises to decide appropriate farming investment projects for their crops and products.

Currently AgBizClimate has a long-term climate tool but no such tool exists for short term climate data. We will implement atool to extract short-term climate data from the Northwest Climate Toolbox database, display it to the user and allow the userto adjust crop yields, inputs and costs. Moreover, a landing tool will be developed to allow users to switch between short termseasonal tool and long-term climate data tool.

## Description of the Problem
The seasonal weather data is important for farmers and land managers as climate may have great impacts on crops. For instance, the precipitation on diﬀerent days across the life cycles of crops may have diﬀerent impacts on the harvest. Land managers and farmers used to rely on past experiences of climate to make decisions for speciﬁc farming operations to reduce the negative impacts and make use of favorable climate conditions. However, these individual experiences of weather data are often limited and inaccurate. Professional tools like software systems could be adopted to build models for decision making based on available seasonal climate data.

AgBizClimate is a sub-project of AgBizLogic (https://www.agbizlogic.com) that works to help farmers and ranchers improve proﬁts by providing constructive advice for decisions on investments and programs. AgBizClimate is designed to deliver essential information about climate change to farmers and land managers regarding their speciﬁc farming operations. However, we need to collect suﬃcient climate data before making any analysis. The aim of this project is to link seasonal weather data from somewhere to AgBizClimate. Speciﬁcally, we plan to transfer and integrate weather data from the Northwest Climate Toolbox database (https://climatetoolbox.org) into AgBizClimate (https://www.agbizlogic.com). We will then use this data for analysis and presentation of the inﬂuence of climate change on costs and returns for farming programs.

Generally, the tool is designed to work as follows. First, the user selects which crops they would like to analyze. Users can choose three to ﬁve diﬀerent crops for analysis. Secondly, users place a pin on a map to select the location where the crops are located. Thirdly, the climate data of the speciﬁed location is plotted and displayed for the user. fourthly, the users would make adjustments to the crops yields, inputs and prices by simple GUI operations. Lastly, the user will make any ﬁnal budget adjustments and will save the budget.

Although it sounds simple, there are several key problems to solve before we can plot data on AgBizClimate web pages. First, the weather data could vary in terms of both format and scale from the Northwest Climate Toolbox. We will need to ensure that the data is collected in a useful format so it will be easier to display. Secondly, the dynamically collected data should be appropriately stored and managed so that it can be ﬂexibly employed in AgBizClimate. Lastly, we will need to ﬁnd a way to plot the data in clear and readable way for our users.

## Proposed Solution

As we have decided the source of the seasonal climate data is Northwest Climate Toolbox (https://climatetoolbox.org). This database provides climate data from around the country in various formats. We will write a tool to retrieve the data from a remote database and store it in the local AgBizClimate server. We will then parse the local climate data, extract the relevant data and process it for display. Finally, the desired climate data is provided to the AgBizClimate application to be displayed to the user.
The main tool we chose is Python, a lightweight and eﬃcient programming language. It is effective at network programming, parsing and transforming various data formats such as XML and JSON. We will use the Django web development frame work to make development quick and simple.

we plan to solve the problems mentioned in the previous section with the following solutions. First, the raw data from the Northwest Climate tool box would be parsed into XML or JSON so it can be easily processed in python. This will also allow us to predeﬁne ﬁeld names for the data making it easier to display. Secondly, we would use database tools like sqlite or MongoDB to store and manage the data. This will make the data easy to process and retrieve by the AgBizClimate application. Lastly, we will use Angular in conjuncture with a plotting library to ensure our graphs are clear and readable.

## Performance Metrics

To ensure that the project is completed to the liking of the client we will complete the criteria shown below. First, climate data for crops shall be retrieved through network (Internet) using programs (scripts) automatically without manual intervention under normal conditions. Once conﬁgured, the programs (scripts) shall be able to run and download any available and desired climate data from the remote climate toolbox server automatically.

Second, it is known that more climate data will be produced over time. The climate data Shall be updated periodically, triggered manually by clicking a button or typing a command on the locally. There will also be conﬁguration ﬁles that will allow the administrator of this system to set how often this data is updated and allow for automatic updates to the data.
Thirdly, The UI shall display the requested climate data in a clear and readable format. The UI shall then allow the user to view and adjust, yields, inputs, prices and budgets. The UI shall then allow the user to export the resulting budget as a pdf ﬁle.
Lastly, these operations should be friendly and useable to both professional and non-professional users and give users warnings or tips if they are making unsafe operations like deleting data ﬁles.



