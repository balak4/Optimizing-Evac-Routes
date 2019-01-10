# Identifying Blocked Roads in Real-Time

## Overview

During disasters, search and rescue teams must be able to search for and get to survivors as fast as possible (in terms of travel time and distance). Current GIS and navigation systems allow responders to calculate travel time and distance between origin and destination, and propose an optimal route to the destination. However, many current platforms do not rely on real-time data (e.g. blocked routes, damaged roads, etc.), leading to inaccurate or inefficient results during (and the immediate period following) a natural disaster. 

This project will leverage social media and potentially other sources (e.g. Waze, Here.com, news feeds) to identify real time road closures or damaged roads, power outages and other blocked routes that may affect the travel time from point A to B during and after a natural disaster.

**Goal:** Allow a user (the public or rescue teams) to search for any of these conditions and identify if and where they exist in a specific location (street, neighborhood, etc.). The output will either be tabular (e.g. search names of closed roads) or geospatial (e.g. a map of real-time blocked roads).

### Directory Structure

- data: contains raw, transformed and final output data
- notebooks: jupyter notebooks
- models: trained models, model predictions, model summaries
- references: data dictionaries, and other explanatory materials.
- reports: final report(s) summarizing project
- src: source code for use in this project


## Team
Bala Krishnamoorthy, Amy Taylor, Brian Brakefield, Veronica Giannota
