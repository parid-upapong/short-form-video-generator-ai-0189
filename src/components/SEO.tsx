import Head from 'next/head';

interface SEOProps {
  title?: string;
  description?: string;
  canonical?: string;
  ogImage?: string;
  ogType?: string;
}

export const SEO = ({
  title = "Viral-Flow AI | Turn Long Videos into Viral TikToks & Reels",
  description = "Transform your podcasts and streams into viral short-form clips in minutes. AI-powered smart cropping, auto-captions, and virality scoring.",
  canonical = "https://viralflow.ai",
  ogImage = "https://viralflow.ai/og-image.png",
  ogType = "website"
}: SEOProps) => {
  const siteName = "Viral-Flow AI";
  const fullTitle = title.includes(siteName) ? title : `${title} | ${siteName}`;

  return (
    <Head>
      <title>{fullTitle}</title>
      <meta name="description" content={description} />
      <link rel="canonical" href={canonical} />
      
      {/* Open Graph */}
      <meta property="og:site_name" content={siteName} />
      <meta property="og:title" content={fullTitle} />
      <meta property="og:description" content={description} />
      <meta property="og:image" content={ogImage} />
      <meta property="og:type" content={ogType} />
      <meta property="og:url" content={canonical} />

      {/* Twitter */}
      <meta name="twitter:card" content="summary_large_image" />
      <meta name="twitter:title" content={fullTitle} />
      <meta name="twitter:description" content={description} />
      <meta name="twitter:image" content={ogImage} />

      {/* Structured Data: SoftwareApplication */}
      <script type="application/ld+json">
        {JSON.stringify({
          "@context": "https://schema.org",
          "@type": "SoftwareApplication",
          "name": "Viral-Flow AI",
          "operatingSystem": "Windows, macOS, Linux, iOS, Android",
          "applicationCategory": "MultimediaApplication",
          "offers": {
            "@type": "Offer",
            "price": "0",
            "priceCurrency": "USD"
          },
          "aggregateRating": {
            "@type": "AggregateRating",
            "ratingValue": "4.9",
            "reviewCount": "1250"
          }
        })}
      </script>
    </Head>
  );
};