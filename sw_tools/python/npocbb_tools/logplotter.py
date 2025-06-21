from plotly.subplots import make_subplots
import plotly
#import plotly.graph_objects as go
import plotly.express as px

def mkplot_devicerun_detail(dfplot,dfbuilt):
    """_summary_

    Args:
        dfplot (_type_): module data to plot
        dfbuilt (_type_): summarized cycle-by-cycle built dataframe
    """
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots
    dfplot['tracelabel'] = dfplot.apply(lambda x: '{:s}_{:s}'.format(x['unit'],x['run'].replace('sample_','')),axis=1);
    if('AmpTemp' in dfplot.columns):
        # this is a power module device
        tracenames  = [
            (('Temps','DegC'),['ValveTemp','AmpTemp','BatteryT']),
            (('PWMs/Pcnts','%'),['ValvePWM','AmpPWM','Batt']),
            #(('SOC','%'),['Batt']),
            (('Volts','Volts'),['BatteryV']),
        ];
    else:
        # this is a sample-prep device sd
        tracenames  = [
            (('Temps','DegC'),['HeaterTemp','BatteryT']),
            (('PWMs/Pcnts','%'),['HeaterPWM','MotorPWM','Battery']),
            (('Motor','RPM'),['MotorSpeed']),
            (('Volts','Volts'),['BatteryV']),
        ];
    facetcol = 'tracelabel';
    xvals = 'runtime';
    nrows = len(tracenames);
    ncols = len(dfplot[facetcol].unique().tolist());

    fig = make_subplots(
        rows=len(tracenames),
        cols=ncols,
        start_cell="top-left",
        shared_xaxes='all', vertical_spacing=0.02, horizontal_spacing=0.02,
        shared_yaxes='rows'
    );

    for row,((subplot_title,ylabel),traces) in enumerate(tracenames):
        print(traces);
        dfmelted = dfplot.melt(
            id_vars=['runtime','tracelabel','run','unit'],
            value_vars=traces,
            var_name='qty'
        );

        # use plotly-express to quickly generate these traces
        figtmp = px.line(
            dfmelted,
            x=xvals,
            y='value',
            hover_data=['run','unit'],
            color='qty',
            facet_col=facetcol,
            markers=True,
        );

        # put the plotly express traces into our greater figure we are assembling (with subplots)
        figtmp.update_traces(legendgroup=row+1,legendgrouptitle_text=subplot_title);
        for trace in figtmp.data:
            c = 1;
            if(trace.xaxis == 'x2'):
                c = 2;
            fig.add_trace(trace, row=row+1,col=c);
        if(row==0):
            # titles at the top of each column
            for cnt,annotation in enumerate(figtmp.layout.annotations):
                fig.add_annotation(
                    text=annotation.text.split('=')[1],
                    xref="x domain", yref="y domain",
                    yanchor='bottom',
                    valign='bottom',x=0.5, y=1.0,
                    #font_size=20,
                    font=dict(weight="bold",size=16),
                    showarrow=False,
                    row=1,col=cnt+1
                );
        if(subplot_title=='Temps' and ('AmpTemp' in dfplot.columns)):
            # for power module...
            # ambient temperature estimation.... take from first value with nonzero runtime
            first_data = dfplot[(dfplot['runtime']<2.0) & (dfplot['runtime']>0)].groupby(facetcol).first()
            for cnt,(grp,firstvals) in enumerate(first_data.iterrows()):
                fig.add_hline(y=firstvals['AmpTemp'],line_width=3, line_dash="dash", line_color="red",
                            showlegend=True,
                            legendgroup=row+1,
                            name='Amp Initial',
                            label_text='Amp initial value {:.1f}degC'.format(firstvals['AmpTemp']),
                            label_yanchor="top",
                            row=row+1,col=cnt+1
                            )
        fig.update_yaxes(title=ylabel,row=row+1,col=1)
        #break;
    
    # force to share same x-axis
    #fig.update_traces(xaxis="x{:}".format(len(tracenames)));

    #fig.update_shapes(selector=dict(type="line"), xref="x2 domain")

    explist = dfplot['expname'].unique().tolist();
    unitlist = dfplot['unit'].unique().tolist();
    runlist = dfplot['run'].unique().tolist();
    if(len(explist)==1):
        # single experiment
        fig.update_layout(title='Exp {:s} (nunits={:d} nruns={:d})'.format(explist[0],len(unitlist),len(runlist)))

    if(len(explist)==1 and len(runlist)==1 and len(unitlist)==1):
        # we are plotting a single run

        # show cycle lines using dfbuilt summary data
        dfcyc = dfbuilt.xs(explist[0],level='expname').xs(unitlist[0],level='unit').xs(runlist[0],level='run')[['TimeEnd','EventEnd']];
        dfcyc['runtime_end'] = (dfcyc['TimeEnd']-dfplot.iloc[0]['Time']).apply(lambda x: x.total_seconds())
        for k,v in dfcyc.iterrows():
            for r in range(nrows):
                label_text = v['EventEnd'];
                if(r!=nrows//2):
                    label_text=None;
                # add vline to middle subplot with label
                fig.add_vline(x=v['runtime_end'],line_width=1, line_dash="dash", line_color="black",
                    showlegend=False,
                    #legendgroup=row+1,
                    #name='Amp Initial',
                    #label_text=v['EventEnd'],
                    label_text=label_text,
                    label_yanchor="bottom",
                    #annotation_text=label_text,
                    #yanchor='middle',
                    row=r
                )
        
        # handle other non-cycle events
        #dfevt = dfplot[(~dfplot['Event'].str.startswith('Cycle')) & (dfplot['Event']!=' ')];
        mask_A = ~(dfplot['Event'].str.startswith('Cycle').convert_dtypes().fillna(False));
        #print('postA');
        mask_B = ~(dfplot['Event'].str.startswith(' ').convert_dtypes().fillna(False));
        dfevt = dfplot[ mask_A &  mask_B ];
    
        print('poost');

    #fig.update_layout(hovermode="y unified")
    fig.update_xaxes(showspikes=True,spikemode='across');
    fig.update_layout(legend=dict(groupclick="toggleitem"))

    # fig.update_layout(
    #     margin=dict(l=20, r=20, t=20, b=20),
    # )
    # set markers and line widths
    fig.update_traces(
        marker=dict(size=4),
        line_width=1.5
    )

    # setup axes and labels labels
    #fig.update_xaxes(dtick=60,scaleanchor='x',scaleratio=1,constrain='domain');
    fig.update_xaxes(nticks=60,range=(0,dfplot.iloc[-1]['runtime']));    # more ticks on x-axes
    fig.update_xaxes(title=xvals+' [seconds]',row=nrows);
    fig.update_yaxes(nticks=20);    # more ticks on y-axes

    # setup legends per row
    for i, yaxis in enumerate(fig.select_yaxes(col=ncols), 1):
        legend_name = f"legend{i}"
        fig.update_layout({legend_name: dict(y=yaxis.domain[1], yanchor="top")}, showlegend=True)
        fig.update_traces(row=i, legend=legend_name)

    # title
    explist = dfplot['expname'].unique().tolist();
    unitlist = dfplot['unit'].unique().tolist();
    runlist = dfplot['run'].unique().tolist();
    fig.update_layout(title='Exps {:s} (nunits={:d} nruns={:d})'.format(str(explist),len(unitlist),len(runlist)))


    #fig.show(renderer='browser')
    #fig.write_html('c:\\TEMP\\NPOCBB_RUN_runtime_{:s}_{:s}_{:s}.html'.format( time.strftime('%Y%m%dT%H%M') ));
    #fig.write_html('c:\\TEMP\\NPOCBB_RUN_runtime_{:s}_{:s}_{:s}.html'.format( explist[0], unitlist[0], runlist[0] ));

    return fig;

def mkplot_runs_timeline(dfruns):
    color_discrete_map={
        "run_success": px.colors.qualitative.Plotly[2], # green
        "run_ended_early_user": "yellow",
        "run_ended_early_other": "orange",
        "bootup": px.colors.qualitative.Plotly[3],  # purple
        "notrun": "gray",
    };

    # hoverdata
    hoverdata_cols = ['unit','expname','run','status','run_expected_sec','CRTCRuntime'];
    hoverdata_cols = [x for x in hoverdata_cols if (x in dfruns.columns)];

    # make timeline bars for successful runs or those that were start but had to end
    dfplt = dfruns[dfruns.status.isin(['run_success','run_ended_early_other','run_ended_early_user'])].reset_index()
    fig = px.timeline(dfplt,
                    x_start="TimeBeg",x_end="TimeEnd",y="unit",
                    color_discrete_map=color_discrete_map,
                    hover_data=hoverdata_cols,
                    color='status',
    );

    # add scatters for other non-success
    dfplt = dfruns[~dfruns.status.isin(['run_success'])].reset_index()
    figtmp = px.strip(dfplt,
                    x="TimeBeg",y="unit",
                    color_discrete_map=color_discrete_map,
                    hover_data=hoverdata_cols,
                    color='status',
                    stripmode='overlay',
    )
    # append traces to previous plotly-express figure
    for trace in figtmp.data:
        fig.add_trace(trace);
    
    # some plot formatting
    fig.update_yaxes(showgrid=True, ticks="outside", tickson="boundaries")
    
    logs_per_day = dfruns.reset_index().set_index('TimeBeg')['run'].resample('D').count();
    
    fig.update_xaxes(
        showgrid=True, ticks="outside", tickson="boundaries",
        rangebreaks=[
            dict(values=[str(x) for x in logs_per_day[logs_per_day==0].index], pattern="hour"), #hide days where it didn't work
        ],
        nticks=50 # hint to plotly express
    )
    
    return fig;