window.dashExtensions = Object.assign({}, window.dashExtensions, {
    default: {
        function0: function(feature, latlng) {
            const flag = L.icon({
                iconUrl: 'assets/logos/hotel.svg',
                iconSize: [25, 25]
            });
            return L.marker(latlng, {
                icon: flag
            });
        },
        function1: function(feature, latlng, context) {
            const {
                circleOptions,
                colorProp
            } = context.hideout;
            const categoryColors = context.hideout.categoryColors; // Agrega esta línea para obtener el diccionario de colores
            const color = categoryColors[feature.properties[colorProp]]; // Si la categoría no tiene un color definido, usa gris
            circleOptions.fillColor = color;
            return L.circleMarker(latlng, circleOptions);
        },
        function2: function(feature, latlng, index, context) {
            const {
                circleOptions,
                colorProp
            } = context.hideout;
            const categoryColors = context.hideout.categoryColors;
            // Set color based on the most frequent category value in the cluster.
            const leaves = index.getLeaves(feature.properties.cluster_id);
            let categoryCounts = {};

            for (let i = 0; i < leaves.length; ++i) {
                const category = leaves[i].properties[colorProp];
                categoryCounts[category] = (categoryCounts[category] || 0) + 1;
            }

            let maxCategory = null;
            let maxCount = 0;

            // Find the most frequent category
            Object.keys(categoryCounts).forEach(category => {
                if (categoryCounts[category] > maxCount) {
                    maxCount = categoryCounts[category];
                    maxCategory = category;
                }
            });

            const color = categoryColors[maxCategory] || 'gray'; // If the category is not defined, use gray

            // Modify icon background color.
            const scatterIcon = L.DivIcon.extend({
                createIcon: function(oldIcon) {
                    let icon = L.DivIcon.prototype.createIcon.call(this, oldIcon);
                    icon.style.backgroundColor = color;
                    return icon;
                }
            });

            // Render a circle with the number of leaves written in the center.
            const icon = new scatterIcon({
                html: '<div style="background-color:white;"><span>' + feature.properties.point_count_abbreviated + '</span></div>',
                className: "marker-cluster",
                iconSize: L.point(40, 40),
                color: color
            });

            return L.marker(latlng, {
                icon: icon
            });
        }
    }
});