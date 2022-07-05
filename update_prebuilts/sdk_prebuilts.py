#!/usr/bin/python3

# This file needs to keep sync with /prebuilts/sdk/update_prebuilts.py

maven_to_make = {
    # AndroidX
    'androidx.benchmark:benchmark-macro': { },
    'androidx.benchmark:benchmark-macro-junit4': { },
    'androidx.benchmark:benchmark-common': { },
    'androidx.benchmark:benchmark-junit4': { },
    'androidx.tracing:tracing': { },
    'androidx.tracing:tracing-ktx': { },
    'androidx.slice:slice-builders': { },
    'androidx.slice:slice-core': { },
    'androidx.slice:slice-view': { },
    'androidx.remotecallback:remotecallback': { },
    'androidx.remotecallback:remotecallback-processor': {'host':True},
    'androidx.versionedparcelable:versionedparcelable': { },
    'androidx.vectordrawable:vectordrawable-animated': { },
    'androidx.activity:activity': { },
    'androidx.activity:activity-ktx': { },
    'androidx.annotation:annotation': {'host_and_device':True},
    'androidx.annotation:annotation-experimental': { },
    'androidx.asynclayoutinflater:asynclayoutinflater': { },
    'androidx.collection:collection': { },
    'androidx.collection:collection-ktx': { },
    'androidx.concurrent:concurrent-futures': { },
    'androidx.concurrent:concurrent-listenablefuture-callback': { },
    'androidx.concurrent:concurrent-listenablefuture': { },
    'androidx.core:core': { },
    'androidx.core:core-animation': { },
    'androidx.core:core-ktx': { },
    'androidx.contentpaging:contentpaging': { },
    'androidx.coordinatorlayout:coordinatorlayout': { },
    'androidx.legacy:legacy-support-core-ui': { },
    'androidx.legacy:legacy-support-core-utils': { },
    'androidx.cursoradapter:cursoradapter': { },
    'androidx.browser:browser': { },
    'androidx.customview:customview': { },
    'androidx.documentfile:documentfile': { },
    'androidx.drawerlayout:drawerlayout': { },
    'androidx.dynamicanimation:dynamicanimation': { },
    'androidx.emoji:emoji': { },
    'androidx.emoji:emoji-appcompat': { },
    'androidx.emoji:emoji-bundled': { },
    'androidx.emoji2:emoji2': { },
    'androidx.emoji2:emoji2-views-helper': { },
    'androidx.exifinterface:exifinterface': { },
    'androidx.fragment:fragment': { },
    'androidx.fragment:fragment-ktx': { },
    'androidx.heifwriter:heifwriter': { },
    'androidx.interpolator:interpolator': { },
    'androidx.loader:loader': { },
    'androidx.localbroadcastmanager:localbroadcastmanager': { },
    'androidx.media:media': { },
    'androidx.media2:media2-player': { },
    'androidx.media2:media2-session': { },
    'androidx.media2:media2-common': { },
    'androidx.media2:media2-exoplayer': { },
    'androidx.media2:media2-widget': { },
    'androidx.navigation:navigation-common': { },
    'androidx.navigation:navigation-common-ktx': { },
    'androidx.navigation:navigation-fragment': { },
    'androidx.navigation:navigation-fragment-ktx': { },
    'androidx.navigation:navigation-runtime': { },
    'androidx.navigation:navigation-runtime-ktx': { },
    'androidx.navigation:navigation-ui': { },
    'androidx.navigation:navigation-ui-ktx': { },
    'androidx.percentlayout:percentlayout': { },
    'androidx.print:print': { },
    'androidx.recommendation:recommendation': { },
    'androidx.recyclerview:recyclerview-selection': { },
    'androidx.savedstate:savedstate': { },
    'androidx.savedstate:savedstate-ktx': { },
    'androidx.slidingpanelayout:slidingpanelayout': { },
    'androidx.swiperefreshlayout:swiperefreshlayout': { },
    'androidx.textclassifier:textclassifier': { },
    'androidx.transition:transition': { },
    'androidx.tvprovider:tvprovider': { },
    'androidx.legacy:legacy-support-v13': { },
    'androidx.legacy:legacy-preference-v14': { },
    'androidx.leanback:leanback': { },
    'androidx.leanback:leanback-preference': { },
    'androidx.legacy:legacy-support-v4': { },
    'androidx.appcompat:appcompat': { },
    'androidx.appcompat:appcompat-resources': { },
    'androidx.cardview:cardview': { },
    'androidx.gridlayout:gridlayout': { },
    'androidx.mediarouter:mediarouter': { },
    'androidx.palette:palette': { },
    'androidx.preference:preference': { },
    'androidx.recyclerview:recyclerview': { },
    'androidx.vectordrawable:vectordrawable': { },
    'androidx.viewpager:viewpager': { },
    'androidx.viewpager2:viewpager2': { },
    'androidx.wear:wear': { },
    'androidx.wear:wear-ongoing': { },
    'androidx.webkit:webkit': { },
    'androidx.biometric:biometric': { },
    'androidx.autofill:autofill': { },
    'androidx.appsearch:appsearch': { },
    'androidx.appsearch:appsearch-local-storage': {'name':'androidx.appsearch_appsearch_local_storage'},
    'androidx.appsearch:appsearch-platform-storage': { },
    'androidx.appsearch:appsearch-compiler': {'name':'androidx.appsearch_appsearch-compiler', 'host':True},
    'androidx.car.app:app': { },
    'androidx.car.app:app-automotive': { },
    'androidx.car.app:app-testing': { },
    'androidx.startup:startup-runtime': { },
    'androidx.resourceinspection:resourceinspection-annotation': { },
    'androidx.profileinstaller:profileinstaller': { },

    # AndroidX for Compose
    'androidx.compose.compiler:compiler-hosted': { 'host':True },
    'androidx.compose.runtime:runtime': { },
    'androidx.compose.runtime:runtime-saveable': { },
    'androidx.compose.foundation:foundation': { },
    'androidx.compose.foundation:foundation-layout': { },
    'androidx.compose.foundation:foundation-text': { },
    'androidx.compose.ui:ui': { },
    'androidx.compose.ui:ui-geometry': { },
    'androidx.compose.ui:ui-graphics': { },
    'androidx.compose.ui:ui-text': { },
    'androidx.compose.ui:ui-unit': { },
    'androidx.compose.ui:ui-util': { },
    'androidx.compose.animation:animation-core': { },
    'androidx.compose.animation:animation': { },
    'androidx.compose.material:material-icons-core': { },
    'androidx.compose.material:material-ripple': { },
    'androidx.compose.material:material': { },
    'androidx.activity:activity-compose': { },

    # AndroidX for Multidex
    'androidx.multidex:multidex': { },
    'androidx.multidex:multidex-instrumentation': { },

    # AndroidX for Constraint Layout
    'androidx.constraintlayout:constraintlayout': {'name':'androidx-constraintlayout_constraintlayout'},
    'androidx.constraintlayout:constraintlayout-solver': {'name':'androidx-constraintlayout_constraintlayout-solver'},

    # AndroidX for Architecture Components
    'androidx.arch.core:core-common': { },
    'androidx.arch.core:core-runtime': { },
    'androidx.lifecycle:lifecycle-common': { },
    'androidx.lifecycle:lifecycle-common-java8': { },
    'androidx.lifecycle:lifecycle-extensions': { },
    'androidx.lifecycle:lifecycle-livedata': { },
    'androidx.lifecycle:lifecycle-livedata-ktx': { },
    'androidx.lifecycle:lifecycle-livedata-core': { },
    'androidx.lifecycle:lifecycle-livedata-core-ktx': { },
    'androidx.lifecycle:lifecycle-process': { },
    'androidx.lifecycle:lifecycle-runtime': { },
    'androidx.lifecycle:lifecycle-runtime-ktx': { },
    'androidx.lifecycle:lifecycle-service': { },
    'androidx.lifecycle:lifecycle-viewmodel': { },
    'androidx.lifecycle:lifecycle-viewmodel-ktx': { },
    'androidx.lifecycle:lifecycle-viewmodel-savedstate': { },
    'androidx.paging:paging-common': { },
    'androidx.paging:paging-common-ktx': { },
    'androidx.paging:paging-runtime': { },
    'androidx.sqlite:sqlite': { },
    'androidx.sqlite:sqlite-framework': { },
    'androidx.room:room-common': {'host_and_device':True},
    'androidx.room:room-compiler': {'host':True, 'extra-static-libs':{'guava-21.0'}},
    'androidx.room:room-migration': {'host_and_device':True},
    'androidx.room:room-runtime': { },
    'androidx.room:room-testing': { },
    'androidx.room:room-compiler-processing': {'host':True},
    'androidx.work:work-runtime': { },
    'androidx.work:work-runtime-ktx': { },
    'androidx.work:work-testing': { },

    # Third-party dependencies
    'com.google.android:flexbox': {'name':'flexbox', 'path':'flexbox'},

    # Androidx Material Design Components
    'com.google.android.material:material': { },
}

# Mapping of POM dependencies to Soong build targets
deps_rewrite = {
    'auto-common':'auto_common',
    'auto-value-annotations':'auto_value_annotations',
    'com.google.auto.value:auto-value':'auto_value_plugin',
    'monitor':'androidx.test.monitor',
    'rules':'androidx.test.rules',
    'runner':'androidx.test.runner',
    'androidx.test:core':'androidx.test.core',
    'com.squareup:javapoet':'javapoet',
    'com.google.guava:listenablefuture':'guava-listenablefuture-prebuilt-jar',
    'sqlite-jdbc':'xerial-sqlite-jdbc',
    'gson':'gson-prebuilt-jar',
    'com.intellij:annotations':'jetbrains-annotations',
    'javax.annotation:javax.annotation-api':'javax-annotation-api-prebuilt-host-jar',
    'org.robolectric:robolectric':'Robolectric_all-target',
    'org.jetbrains.kotlin:kotlin-stdlib-common':'kotlin-stdlib',
    'org.jetbrains.kotlinx:kotlinx-coroutines-core':'kotlinx_coroutines',
    'org.jetbrains.kotlinx:kotlinx-coroutines-android':'kotlinx_coroutines_android',
    'org.jetbrains.kotlinx:kotlinx-metadata-jvm':'kotlinx_metadata_jvm',
}
