import React from 'react';
import './CardChart.css';

const CardChart = ({ title = 'Chart', labels = [], data = [] }) => {
  const maxValue = Math.max(0, ...data);
  const chartItems = labels.length
    ? labels.map((label, index) => ({ label, value: data[index] ?? 0 }))
    : data.map((value, index) => ({ label: `Value ${index + 1}`, value }));

  return (
    <section className="card-chart" aria-label={title}>
      <h2 className="card-chart__title">{title}</h2>
      <div className="card-chart__chart">
        {chartItems.map((item, index) => (
          <div
            key={item.label || index}
            className="card-chart__bar"
            style={{ height: `${maxValue ? (item.value / maxValue) * 100 : 0}%` }}
            title={`${item.label}: ${item.value}`}
          >
            <span className="card-chart__label">{item.label}</span>
          </div>
        ))}
      </div>
    </section>
  );
};

export { CardChart };
export default CardChart;
