function getTracks() {
  const genre = document.getElementById("genre").value;
  fetch(`/tracks/${genre}`)
    .then((response) => response.json())
    .then((data) => displayTracks(data))
    .catch((error) => console.error("Error:", error));
}

function displayTracks(tracks) {
  const tableBody = document.getElementById("tracksBody");
  tableBody.innerHTML = "";

  for (const track of tracks) {
    const row = document.createElement("tr");

    const artistCell = document.createElement("td");
    artistCell.textContent = track.artist;

    const trackCell = document.createElement("td");
    trackCell.textContent = track.track;

    const popularityCell = document.createElement("td");
    popularityCell.className = "popularity-cell";
    popularityCell.textContent = track.popularity + "%";
    popularityCell.style.backgroundColor = getPopularityColor(track.popularity);

    const albumCoverCell = document.createElement("td");
    const albumCoverImage = document.createElement("img");
    albumCoverImage.src = track.album_image_url;
    albumCoverImage.alt = `${track.artist} - ${track.track}`;
    albumCoverCell.appendChild(albumCoverImage);

    const previewCell = document.createElement("td");
    previewCell.className = "preview-cell";

    if (track.preview_url) {
      const previewLink = document.createElement("a");
      previewLink.textContent = "Preview";
      previewLink.href = track.preview_url;
      previewCell.appendChild(previewLink);
    } else {
      // If preview URL doesn't exist, display a tilde (~) to indicate absence
      previewCell.textContent = "~";
    }

    row.appendChild(artistCell);
    row.appendChild(trackCell);
    row.appendChild(popularityCell);
    row.appendChild(albumCoverCell);
    row.appendChild(previewCell);

    tableBody.appendChild(row);
  }
}
function getPopularityColor(popularity) {
  // Calculate RGB values for the color gradient (from red to green)
  const minPopularity = 0;
  const maxPopularity = 100;
  const red = 255;
  const green = 0;
  const blue = 0;

  const normalizedPopularity =
    (popularity - minPopularity) / (maxPopularity - minPopularity);
  const r = Math.round(red + normalizedPopularity * (green - red));
  const g = Math.round(green - normalizedPopularity * (green - red));
  const b = blue;

  return `rgb(${r},${g},${b})`;
}
